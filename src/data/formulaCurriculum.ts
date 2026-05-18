import type { Course, Quiz } from '../hooks/useEducation';
import formulaBank from './formulaBank.json';

type FormulaBank = Record<Course['syllabusId'], Record<string, { source: string; lines: string[] }>>;

interface FormulaEntry {
  topic: string;
  formula: string;
  example?: string;
}

const typedFormulaBank = formulaBank as FormulaBank;

const slugify = (value: string) =>
  value
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '_')
    .replace(/^_+|_+$/g, '');

const hashString = (value: string) => {
  let hash = 0;
  for (let index = 0; index < value.length; index += 1) {
    hash = (hash * 31 + value.charCodeAt(index)) >>> 0;
  }
  return hash;
};

const isHeadingLine = (line: string) =>
  line.length <= 70 &&
  !line.includes('→') &&
  !/[=+\-−×÷<>]/.test(line) &&
  !/^syllabus topics?$/i.test(line);

const stripNumberPrefix = (value: string) =>
  value.replace(/^\d+\.\s*/, '').trim();

const cleanLine = (line: string) =>
  line
    .replace(/👉\s*/g, '')
    .replace(/([A-Za-z0-9)\]}>])Example\b/g, '$1 Example')
    .replace(/Example\s*→/gi, 'Example →')
    .replace(/Example\s*:/gi, 'Example →')
    .replace(/Formula\s*→/gi, 'Formula →')
    .replace(/\s+/g, ' ')
    .trim();

const parseFormulaEntries = (lines: string[]): FormulaEntry[] => {
  let currentTopic = 'Formula Practice';
  const entries: FormulaEntry[] = [];

  lines.slice(1).forEach((rawLine) => {
    const line = cleanLine(rawLine);
    if (!line || /^syllabus$/i.test(line) || /^syllabus topics?$/i.test(line)) return;

    if (isHeadingLine(line)) {
      currentTopic = stripNumberPrefix(line);
      return;
    }

    const exampleMatch = line.match(/Example\s*(?:→)?\s*(.+)$/i);
    const example = exampleMatch?.[1]?.trim();
    const formulaPart = (exampleMatch ? line.slice(0, exampleMatch.index).trim() : line)
      .replace(/^Formula →\s*/i, '')
      .trim();

    if (!formulaPart) {
      const lastEntry = entries[entries.length - 1];
      if (lastEntry && example && !lastEntry.example) {
        lastEntry.example = example;
      }
      return;
    }

    const arrowIndex = formulaPart.indexOf('→');
    const hasLabelledFormula = arrowIndex > 0 && arrowIndex < 45;
    const topic = hasLabelledFormula
      ? stripNumberPrefix(formulaPart.slice(0, arrowIndex).trim())
      : currentTopic;
    const formula = hasLabelledFormula
      ? formulaPart.slice(arrowIndex + 1).trim()
      : formulaPart;

    entries.push({
      topic,
      formula: stripNumberPrefix(formula),
      example
    });
  });

  return entries;
};

const getFormulaEntries = (syllabusId: Course['syllabusId'], grade: string) =>
  parseFormulaEntries(typedFormulaBank[syllabusId]?.[grade]?.lines || []);

const scoreEntry = (entry: FormulaEntry, keywords: string[]) => {
  const haystack = `${entry.topic} ${entry.formula} ${entry.example || ''}`.toLowerCase();
  return keywords.reduce((score, keyword) => score + (haystack.includes(keyword) ? 1 : 0), 0);
};

export const selectFormulaEntries = (
  syllabusId: Course['syllabusId'],
  grade: string,
  moduleTitle: string,
  chapterName = '',
  count = 3
) => {
  const entries = getFormulaEntries(syllabusId, grade);
  if (entries.length === 0) return [];

  const keywords = `${moduleTitle} ${chapterName}`
    .toLowerCase()
    .split(/[^a-z0-9]+/)
    .filter(word => word.length > 2);

  const ranked = entries
    .map((entry, index) => ({ entry, index, score: scoreEntry(entry, keywords) }))
    .sort((a, b) => b.score - a.score || a.index - b.index);

  const matched = ranked.filter(item => item.score > 0).map(item => item.entry);
  if (matched.length >= count) return matched.slice(0, count);

  const start = hashString(`${syllabusId}_${grade}_${moduleTitle}_${chapterName}`) % entries.length;
  const selected = [...matched];
  for (let offset = 0; selected.length < count && offset < entries.length; offset += 1) {
    const entry = entries[(start + offset) % entries.length];
    if (!selected.some(item => item.formula === entry.formula)) selected.push(entry);
  }

  return selected;
};

const optionSet = (correctAnswer: string, distractors: string[], seed: string) => {
  const unique = [correctAnswer, ...distractors.filter(item => item && item !== correctAnswer)]
    .filter((item, index, items) => items.indexOf(item) === index)
    .slice(0, 4);

  while (unique.length < 4) {
    unique.push(`Practice step ${unique.length}`);
  }

  const offset = hashString(seed) % unique.length;
  return [...unique.slice(offset), ...unique.slice(0, offset)];
};

const makePracticePrompt = (entry: FormulaEntry, index: number) =>
  entry.example
    ? `Change one number in this example and solve again: ${entry.example}`
    : `Apply formula ${index + 1} to one new sum and check each step.`;

const buildExampleSteps = (entry: FormulaEntry) => {
  const example = entry.example || 'Choose simple values, substitute them, and simplify.';
  const [calculation, result] = example.split('=').map(part => part.trim());
  return [
    `1. Write the formula: ${entry.formula}`,
    `2. Read the given values from the example: ${example}`,
    `3. Substitute the values into the formula: ${calculation || example}`,
    `4. Simplify carefully${result ? ` to get ${result}` : ' until you get the answer'}.`,
    `5. Check the final answer with the operation, sign, unit, or place value.`
  ].join('\n');
};

const visualForTopic = (topic: string) => {
  const lower = topic.toLowerCase();
  if (/angle|triangle|circle|shape|area|perimeter|volume|geometry|mensuration/.test(lower)) {
    return '/concept-visuals/geometry-formula.svg';
  }
  if (/equation|algebra|polynomial|function|linear|quadratic|matrix|sets/.test(lower)) {
    return '/concept-visuals/algebra-formula.svg';
  }
  if (/data|mean|median|mode|probability|statistics/.test(lower)) {
    return '/concept-visuals/data-formula.svg';
  }
  return '/concept-visuals/number-formula.svg';
};

export const buildFormulaLessonContent = ({
  syllabusId,
  grade,
  moduleTitle,
  chapterName,
  difficulty,
  timerMinutes
}: {
  syllabusId: Course['syllabusId'];
  grade: string;
  moduleTitle: string;
  chapterName?: string;
  difficulty?: string;
  timerMinutes?: number;
}) => {
  const entries = selectFormulaEntries(syllabusId, grade, moduleTitle, chapterName, 4);

  if (entries.length === 0) {
    return `# ${moduleTitle}\n\n## Formula Focus\nUse the key formula, study the example sum, and solve more practice sums before the quiz.\n\n[QUIZ_PLACEHOLDER]`;
  }

  const formulaSections = entries.map((entry, index) => (
    `### ${entry.topic}\n![${entry.topic} visual model](${visualForTopic(entry.topic)})\nFormula: ${entry.formula}\nExample sum: ${entry.example || 'Create a simple value substitution and solve step by step.'}\nClear step-by-step solving:\n${buildExampleSteps(entry)}\nPractice sum: ${makePracticePrompt(entry, index)}`
  ));

  const quickCheck = entries[0];
  const alternate = entries[1] || entries[0];

  return [
    `# ${moduleTitle}`,
    `## Formula Focus`,
    `Skip the long theory. Study the formula, follow the example sum, and then solve the extra formula-based sums.`,
    ...formulaSections,
    `## More Formula Based Sums`,
    ...entries.map((entry, index) => `${index + 1}. ${makePracticePrompt(entry, index)}`),
    `:::check Quick Formula Check ::: Which formula should you use for ${quickCheck.topic}? ::: *${quickCheck.formula} | ${alternate.formula} ::: Use the matching formula first, then substitute the values from the sum. :::`,
    difficulty ? `Difficulty: ${difficulty}` : '',
    timerMinutes ? `Estimated timer: ${timerMinutes} minutes.` : '',
    `[QUIZ_PLACEHOLDER]`
  ].filter(Boolean).join('\n\n');
};

export const buildFormulaQuestions = ({
  syllabusId,
  grade,
  moduleTitle,
  chapterName,
  idPrefix,
  points = 10
}: {
  syllabusId: Course['syllabusId'];
  grade: string;
  moduleTitle: string;
  chapterName?: string;
  idPrefix: string;
  points?: number;
}): Quiz['questions'] => {
  const selected = selectFormulaEntries(syllabusId, grade, moduleTitle, chapterName, 4);
  const allEntries = getFormulaEntries(syllabusId, grade);
  if (selected.length === 0 || allEntries.length === 0) return [];

  return selected.flatMap((entry, index) => {
    const distractorFormulas = allEntries
      .filter(item => item.formula !== entry.formula)
      .map(item => item.formula);

    const questions: Quiz['questions'] = [{
      id: `${idPrefix}_formula_${index + 1}`,
      type: 'mcq',
      text: `Which formula is best for ${entry.topic} sums in ${moduleTitle}?`,
      options: optionSet(entry.formula, distractorFormulas, `${idPrefix}_${entry.topic}`),
      correctAnswer: entry.formula,
      points,
      rationale: `Use ${entry.formula} for ${entry.topic} formula-based sums.`
    }];

    if (entry.example) {
      const distractorExamples = allEntries
        .filter(item => item.example && item.example !== entry.example)
        .map(item => item.example as string);

      questions.push({
        id: `${idPrefix}_example_${index + 1}`,
        type: 'mcq',
        text: `Which example sum matches ${entry.topic}?`,
        options: optionSet(entry.example, distractorExamples, `${idPrefix}_${entry.topic}_example`),
        correctAnswer: entry.example,
        points,
        rationale: `This example shows how to substitute values into the formula: ${entry.formula}.`
      });
    }

    return questions;
  });
};

export const formulaTagsFor = (syllabusId: Course['syllabusId'], grade: string) => {
  const source = typedFormulaBank[syllabusId]?.[grade]?.source;
  return source ? ['Formula Based', source.split('/').pop() || 'Formula Source'] : ['Formula Based'];
};

export const getStudyMaterialPath = (syllabusId: Course['syllabusId'], grade: string) => {
  const source = typedFormulaBank[syllabusId]?.[grade]?.source;
  return source ? `/study-materials/${source}` : '';
};
