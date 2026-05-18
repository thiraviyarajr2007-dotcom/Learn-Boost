import type { UserProfile } from '../context/AuthContext';
import type { Course, Module, Quiz } from '../hooks/useEducation';
import { normalizeClass12MathCurriculum, normalizeStrictCurriculum, StrictCurriculumChapter } from './curriculumNormalizer';
import { buildFormulaLessonContent, buildFormulaQuestions, formulaTagsFor } from './formulaCurriculum';
import { TN_CLASS_1_EVS, TN_CLASS_1_MATH, TN_CLASS_2_EVS, TN_CLASS_2_MATH, TN_CLASS_3_EVS, TN_CLASS_3_MATH, TermSyllabus } from './tn_syllabus';

import cbseClass1 from './cbse_class1_mathematics_learning_journey.json';
import cbseClass2 from './cbse_class2_mathematics_learning_journey.json';
import cbseClass3 from './cbse_class3_mathematics_learning_journey.json';
import cbseClass4 from './cbse_class4_mathematics_learning_journey.json';
import cbseClass5 from './cbse_class5_mathematics_learning_journey.json';
import cbseClass6 from './cbse_class6_mathematics_learning_journey.json';
import cbseClass7 from './cbse_class7_mathematics_learning_journey.json';
import cbseClass8 from './cbse_class8_mathematics_learning_journey.json';
import cbseClass9 from './cbse_class9_mathematics_learning_journey.json';
import cbseClass10 from './cbse_class10_mathematics_learning_journey.json';
import cbseClass11 from './cbse_class11_mathematics_learning_journey.json';
import cbseClass12 from './cbse_class12_mathematics_learning_journey.json';
import tnClass12Math from './class12_mathematics_learning_journey.json';

export interface BundledCurriculum {
  courses: Course[];
  modulesByCourseId: Record<string, Module[]>;
  quizzesByCourseId: Record<string, Quiz[]>;
}

type CurriculumJson = StrictCurriculumChapter[] | { chapters: StrictCurriculumChapter[] };

const SYSTEM_TEACHER_ID = 'bundled-curriculum';

export const cbseCurriculumByGrade: Record<string, CurriculumJson> = {
  'Class 1': cbseClass1 as CurriculumJson,
  'Class 2': cbseClass2 as CurriculumJson,
  'Class 3': cbseClass3 as CurriculumJson,
  'Class 4': cbseClass4 as CurriculumJson,
  'Class 5': cbseClass5 as CurriculumJson,
  'Class 6': cbseClass6 as CurriculumJson,
  'Class 7': cbseClass7 as CurriculumJson,
  'Class 8': cbseClass8 as CurriculumJson,
  'Class 9': cbseClass9 as CurriculumJson,
  'Class 10': cbseClass10 as CurriculumJson,
  'Class 11': cbseClass11 as CurriculumJson,
  'Class 12': cbseClass12 as CurriculumJson
};

export { tnClass12Math };

const tnPrimaryByGrade: Partial<Record<string, Array<{ name: string; data: TermSyllabus[] }>>> = {
  'Class 1': [{ name: 'Mathematics', data: TN_CLASS_1_MATH }, { name: 'Environmental Science', data: TN_CLASS_1_EVS }],
  'Class 2': [{ name: 'Mathematics', data: TN_CLASS_2_MATH }, { name: 'Environmental Science', data: TN_CLASS_2_EVS }],
  'Class 3': [{ name: 'Mathematics', data: TN_CLASS_3_MATH }, { name: 'Environmental Science', data: TN_CLASS_3_EVS }]
};

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
    const swapIndex = 1 + (hashString(`${seed}_${correctAnswer}`) % (rotated.length - 1));
    [rotated[0], rotated[swapIndex]] = [rotated[swapIndex], rotated[0]];
  }

  return rotated;
};

const chaptersFrom = (json: CurriculumJson) => Array.isArray(json) ? json : json.chapters;

const emptyBundle = (): BundledCurriculum => ({
  courses: [],
  modulesByCourseId: {},
  quizzesByCourseId: {}
});

const addNormalized = (bundle: BundledCurriculum, normalizedCourses: ReturnType<typeof normalizeStrictCurriculum>) => {
  normalizedCourses.forEach(({ course, modules, quizzes }) => {
    bundle.courses.push(course);
    bundle.modulesByCourseId[course.id] = modules;
    bundle.quizzesByCourseId[course.id] = quizzes;
  });
};

const makeQuestion = (id: string, topic: string, subject: string): Quiz['questions'][number] => {
  const correctAnswer = 'Understand the idea';
  return {
    id,
    type: 'mcq',
    text: `What is the best first step while learning ${topic} in ${subject}?`,
    options: rotateOptions(
      [correctAnswer, 'Skip practice', 'Guess quickly', 'Ignore examples'],
      correctAnswer,
      `${subject}_${topic}_${id}`
    ),
    correctAnswer,
    points: 10,
    rationale: 'A clear concept makes practice and quiz questions easier.'
  };
};

const makeTnTermBundle = (
  grade: string,
  subjects: Array<{ name: string; data: TermSyllabus[] }>,
  termMode: 'terms' | 'full-year'
) => {
  const bundle = emptyBundle();

  subjects.forEach((subject) => {
    subject.data.forEach((termInfo) => {
      const groupedUnits = termMode === 'full-year'
        ? [{ ...termInfo, term: 'Full Year' as const }]
        : [termInfo];

      groupedUnits.forEach((group) => {
        group.units.forEach((unit) => {
          const term = group.term;
          const courseId = `tn_board_${slugify(grade)}_${slugify(subject.name)}_${slugify(term)}_${slugify(unit.title)}`;
          const course: Course = {
            id: courseId,
            title: `${subject.name}: ${unit.title} (${term})`,
            description: subject.name === 'Mathematics'
              ? `Formula, example-sum, and practice-sum path for ${grade} ${unit.title}.`
              : unit.description,
            syllabusId: 'TN State Board',
            grade,
            term,
            subject: subject.name,
            teacherId: SYSTEM_TEACHER_ID,
            coverImage: '',
            tags: subject.name === 'Mathematics'
              ? [subject.name, unit.title, term, grade, 'Bundled', ...formulaTagsFor('TN State Board', grade)]
              : [subject.name, unit.title, term, grade, 'Bundled'],
            moduleCount: unit.topics.length
          };

          const modules = unit.topics.map((topic, index): Module => {
            const content = subject.name === 'Mathematics'
              ? buildFormulaLessonContent({
                  syllabusId: 'TN State Board',
                  grade,
                  moduleTitle: topic,
                  chapterName: unit.title,
                  difficulty: index === unit.topics.length - 1 ? 'Medium' : 'Easy',
                  timerMinutes: 8
                })
              : `# ${topic}\n\n${unit.description}\n\nLearn the core idea, study one example, and then solve the practice challenge for ${topic} in ${subject.name}.\n\n[QUIZ_PLACEHOLDER]`;

            return {
              id: `${courseId}_mod_${index + 1}`,
              courseId,
              title: topic,
              content: content,
              order: index + 1,
              tags: subject.name === 'Mathematics'
                ? [subject.name, topic, grade, term, ...formulaTagsFor('TN State Board', grade)]
                : [subject.name, topic, grade, term]
            };
          });

          const quizzes = modules.map((module): Quiz => {
            const moduleDifficulty = module.order === modules.length ? 'Medium' : 'Easy';
            const defaultQuestions = [
              makeQuestion('q1', module.title, subject.name),
              {
                ...makeQuestion('q2', module.title, subject.name),
                id: 'q2',
                text: `After studying ${module.title}, what should you do next?`,
                options: rotateOptions(
                  ['Try practice questions', 'Close the lesson', 'Change board', 'Skip the quiz'],
                  'Try practice questions',
                  `${subject.name}_${module.title}_q2`
                ),
                correctAnswer: 'Try practice questions'
              }
            ];
            const formulaQuestions = subject.name === 'Mathematics'
              ? buildFormulaQuestions({
                  syllabusId: 'TN State Board',
                  grade,
                  moduleTitle: module.title,
                  chapterName: unit.title,
                  idPrefix: slugify(module.id),
                  points: 10
                })
              : [];
            const questions = subject.name === 'Mathematics'
              ? [...formulaQuestions, ...defaultQuestions]
              : defaultQuestions;

            return {
              id: `quiz_${module.id}`,
              courseId,
              moduleId: module.id,
              title: `${module.title} Check`,
              totalPoints: questions.reduce((total, question) => total + question.points, 0),
              timerPerQuestion: moduleDifficulty === 'Medium' ? 60 : 40,
              questions
            };
          });

          bundle.courses.push(course);
          bundle.modulesByCourseId[courseId] = modules;
          bundle.quizzesByCourseId[courseId] = quizzes;
        });
      });
    });
  });

  return bundle;
};

const genericTnSyllabus = (grade: string, subjectName: string): TermSyllabus[] => {
  const subjectTopics = subjectName === 'Environmental Science'
    ? [
        ['Living World', ['Plants around us', 'Animals and habitats', 'Food chains']],
        ['Our Environment', ['Air and water', 'Weather and seasons', 'Keeping surroundings clean']],
        ['Health and Society', ['Healthy habits', 'Safety rules', 'Community helpers']]
      ]
    : [
        ['Number System', ['Numbers and operations', 'Factors and multiples', 'Fractions and decimals']],
        ['Geometry and Measurement', ['Lines and angles', 'Shapes and solids', 'Perimeter area and volume']],
        ['Data and Problem Solving', ['Patterns', 'Data handling', 'Everyday word problems']]
      ];

  return subjectTopics.map(([title, topics], index) => ({
    term: `Term ${index + 1}` as TermSyllabus['term'],
    units: [{
      title: title as string,
      topics: topics as string[],
      description: `${grade} TN State Board ${subjectName} learning path for ${title}.`
    }]
  }));
};

export const getBundledCurriculum = (profile: Pick<UserProfile, 'syllabus' | 'grade'> | null): BundledCurriculum => {
  if (!profile?.syllabus || !profile.grade) return emptyBundle();

  const bundle = emptyBundle();

  if (profile.syllabus === 'CBSE') {
    const curriculum = cbseCurriculumByGrade[profile.grade];
    if (!curriculum) return bundle;

    addNormalized(bundle, normalizeStrictCurriculum(
      chaptersFrom(curriculum),
      SYSTEM_TEACHER_ID,
      {
        syllabusId: 'CBSE',
        grade: profile.grade,
        subject: 'Mathematics',
        term: 'Full Year',
        descriptionPrefix: 'Bundled CBSE Mathematics learning journey',
        tags: ['NCERT', 'Bundled']
      }
    ));
    return bundle;
  }

  if (profile.grade === 'Class 12') {
    addNormalized(bundle, normalizeClass12MathCurriculum(
      tnClass12Math as StrictCurriculumChapter[],
      SYSTEM_TEACHER_ID
    ));
    return bundle;
  }

  const classNumber = Number(profile.grade.replace(/\D/g, ''));
  const primarySubjects = tnPrimaryByGrade[profile.grade];
  const subjects = primarySubjects || [
    { name: 'Mathematics', data: genericTnSyllabus(profile.grade, 'Mathematics') },
    ...(classNumber <= 8 ? [{ name: 'Environmental Science', data: genericTnSyllabus(profile.grade, 'Environmental Science') }] : [])
  ];

  return makeTnTermBundle(profile.grade, subjects, classNumber >= 9 ? 'full-year' : 'terms');
};
