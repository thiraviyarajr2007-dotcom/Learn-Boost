import type { Course, Module, Quiz } from '../hooks/useEducation';
import { buildFormulaLessonContent, buildFormulaQuestions, formulaTagsFor } from './formulaCurriculum';

export interface StrictCurriculumQuestion {
  question_id: number | string;
  question_text: string;
  options: string[];
  correct_answer: string;
  rationale: string;
  timer_per_question_seconds: number;
}

export interface StrictCurriculumModule {
  module_id: number | string;
  topic_name: string;
  explanation: string;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  total_timer_minutes: number;
  questions: StrictCurriculumQuestion[];
}

export interface StrictCurriculumChapter {
  chapter_name: string;
  modules: StrictCurriculumModule[];
}

export interface NormalizedCurriculumCourse {
  course: Course & {
    createdAt?: unknown;
    updatedAt?: unknown;
  };
  modules: Module[];
  quizzes: Quiz[];
}

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

const rotateOptions = (options: string[], correctAnswer: string, seed: string) => {
  if (options.length <= 1) return options;

  const rotated = [...options];
  const offset = hashString(seed) % rotated.length;
  for (let index = 0; index < offset; index += 1) {
    const first = rotated.shift();
    if (first !== undefined) rotated.push(first);
  }

  if (rotated[0] === correctAnswer) {
    const swapIndex = rotated.length > 1 ? 1 + (hashString(`${seed}_${correctAnswer}`) % (rotated.length - 1)) : 0;
    [rotated[0], rotated[swapIndex]] = [rotated[swapIndex], rotated[0]];
  }

  return rotated;
};

const getChapterMeta = (chapterIndex: number) => {
  const isVolumeOne = chapterIndex < 6;
  const months = [
    'June',
    'July',
    'July',
    'July/August',
    'August',
    'August/September',
    'October',
    'October/November',
    'November/December',
    'December/January',
    'January',
    'January'
  ];

  return {
    volume: isVolumeOne ? 'Volume 1' : 'Volume 2',
    month: months[chapterIndex] || 'Full Year'
  };
};

const timerForDifficulty = (difficulty: StrictCurriculumModule['difficulty']) => {
  if (difficulty === 'Hard') return 90;
  if (difficulty === 'Medium') return 60;
  return 40;
};

export interface CurriculumScope {
  syllabusId: Course['syllabusId'];
  grade: string;
  subject: string;
  term: Course['term'];
  descriptionPrefix?: string;
  tags?: string[];
}

export const normalizeStrictCurriculum = (
  curriculum: StrictCurriculumChapter[],
  teacherId: string,
  scope: CurriculumScope
): NormalizedCurriculumCourse[] => {
  const boardSlug = slugify(scope.syllabusId);
  const gradeSlug = slugify(scope.grade);
  const subjectSlug = slugify(scope.subject);
  const termSlug = slugify(scope.term);

  return curriculum.map((chapter, chapterIndex) => {
    const chapterNumber = chapterIndex + 1;
    const courseId = `${boardSlug}_${gradeSlug}_${subjectSlug}_${termSlug}_ch_${String(chapterNumber).padStart(2, '0')}_${slugify(chapter.chapter_name)}`;
    const commonTags = [
      scope.grade,
      scope.subject,
      scope.syllabusId,
      scope.term,
      `Chapter ${chapterNumber}`,
      ...(scope.tags || [])
    ];

    const course: NormalizedCurriculumCourse['course'] = {
      id: courseId,
      title: `${scope.subject}: Chapter ${chapterNumber} - ${chapter.chapter_name}`,
      description: `Formula, example-sum, and practice-sum learning path for ${scope.syllabusId} ${scope.grade} ${scope.subject}: ${chapter.chapter_name}.`,
      syllabusId: scope.syllabusId,
      grade: scope.grade,
      term: scope.term,
      subject: scope.subject,
      teacherId,
      coverImage: '',
      tags: [...commonTags, ...formulaTagsFor(scope.syllabusId, scope.grade)],
      moduleCount: chapter.modules.length
    };

    const modules: Module[] = chapter.modules.map((module, moduleIndex) => {
      const interactiveContent = buildFormulaLessonContent({
        syllabusId: scope.syllabusId,
        grade: scope.grade,
        moduleTitle: module.topic_name,
        chapterName: chapter.chapter_name,
        difficulty: module.difficulty,
        timerMinutes: module.total_timer_minutes
      });

      return {
        id: String(module.module_id),
        courseId,
        title: module.topic_name,
        content: interactiveContent,
        order: moduleIndex + 1,
        tags: [...commonTags, chapter.chapter_name, module.difficulty, ...formulaTagsFor(scope.syllabusId, scope.grade)],
        explanation: module.explanation
      };
    });

    const quizzes: Quiz[] = chapter.modules.map((module) => {
      const existingQuestions = module.questions.map((question) => ({
        id: `q_${question.question_id}`,
        type: 'mcq' as const,
        text: question.question_text,
        options: rotateOptions(question.options, question.correct_answer, `${module.module_id}_${question.question_id}`),
        correctAnswer: question.correct_answer,
        points: module.difficulty === 'Hard' ? 15 : module.difficulty === 'Medium' ? 10 : 5,
        rationale: question.rationale
      }));
      const formulaQuestions = buildFormulaQuestions({
        syllabusId: scope.syllabusId,
        grade: scope.grade,
        moduleTitle: module.topic_name,
        chapterName: chapter.chapter_name,
        idPrefix: slugify(String(module.module_id)),
        points: module.difficulty === 'Hard' ? 15 : module.difficulty === 'Medium' ? 10 : 5
      });
      const questions = [...formulaQuestions, ...existingQuestions];

      return {
        id: `quiz_${module.module_id}`,
        courseId,
        moduleId: String(module.module_id),
        title: `${module.topic_name} Challenge`,
        totalPoints: questions.reduce((sum, question) => sum + question.points, 0),
        timerPerQuestion: timerForDifficulty(module.difficulty),
        questions
      };
    });

    return { course, modules, quizzes };
  });
};

export const normalizeClass12MathCurriculum = (
  curriculum: StrictCurriculumChapter[],
  teacherId: string
): NormalizedCurriculumCourse[] => {
  return curriculum.map((chapter, chapterIndex) => {
    const chapterNumber = chapterIndex + 1;
    const meta = getChapterMeta(chapterIndex);
    const courseId = `tn_board_class_12_mathematics_full_year_ch_${String(chapterNumber).padStart(2, '0')}_${slugify(chapter.chapter_name)}`;

    const course: NormalizedCurriculumCourse['course'] = {
      id: courseId,
      title: `Mathematics: Chapter ${chapterNumber} - ${chapter.chapter_name}`,
      description: `Formula, example-sum, and practice-sum learning path for TN State Board Class 12 Mathematics: ${chapter.chapter_name}.`,
      syllabusId: 'TN State Board',
      grade: 'Class 12',
      term: 'Full Year',
      subject: 'Mathematics',
      teacherId,
      coverImage: '',
      tags: ['Class 12', 'Mathematics', 'TN State Board', meta.volume, meta.month, `Chapter ${chapterNumber}`, ...formulaTagsFor('TN State Board', 'Class 12')],
      moduleCount: chapter.modules.length
    };

    const modules: Module[] = chapter.modules.map((module, moduleIndex) => {
      const interactiveContent = buildFormulaLessonContent({
        syllabusId: 'TN State Board',
        grade: 'Class 12',
        moduleTitle: module.topic_name,
        chapterName: chapter.chapter_name,
        difficulty: module.difficulty,
        timerMinutes: module.total_timer_minutes
      });

      return {
        id: String(module.module_id),
        courseId,
        title: module.topic_name,
        content: interactiveContent,
        order: moduleIndex + 1,
        tags: ['Class 12', 'Mathematics', chapter.chapter_name, module.difficulty, meta.volume, meta.month, ...formulaTagsFor('TN State Board', 'Class 12')],
        explanation: module.explanation
      };
    });

    const quizzes: Quiz[] = chapter.modules.map((module) => {
      const existingQuestions = module.questions.map((question) => ({
        id: `q_${question.question_id}`,
        type: 'mcq' as const,
        text: question.question_text,
        options: rotateOptions(question.options, question.correct_answer, `${module.module_id}_${question.question_id}`),
        correctAnswer: question.correct_answer,
        points: module.difficulty === 'Hard' ? 15 : module.difficulty === 'Medium' ? 10 : 5,
        rationale: question.rationale
      }));
      const formulaQuestions = buildFormulaQuestions({
        syllabusId: 'TN State Board',
        grade: 'Class 12',
        moduleTitle: module.topic_name,
        chapterName: chapter.chapter_name,
        idPrefix: slugify(String(module.module_id)),
        points: module.difficulty === 'Hard' ? 15 : module.difficulty === 'Medium' ? 10 : 5
      });
      const questions = [...formulaQuestions, ...existingQuestions];

      return {
        id: `quiz_${module.module_id}`,
        courseId,
        moduleId: String(module.module_id),
        title: `${module.topic_name} Challenge`,
        totalPoints: questions.reduce((sum, question) => sum + question.points, 0),
        timerPerQuestion: timerForDifficulty(module.difficulty),
        questions
      };
    });

    return { course, modules, quizzes };
  });
};
