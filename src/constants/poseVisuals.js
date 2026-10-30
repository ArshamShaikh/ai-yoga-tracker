/**
 * poseVisuals.js
 * Visual icons, step-by-step execution guides, and anatomical benefits
 * for yoga poses to provide educational pre-session context.
 */

export const POSE_METADATA = {
    tadasana: {
        icon: 'male',
        categoryTag: 'Foundation',
        accentColor: '#10B981',
        instructions: [
            'Stand tall with feet together or hip-width apart.',
            'Distribute body weight evenly across both feet.',
            'Engage quadriceps, draw tailbone down slightly, and tuck pelvis.',
            'Roll shoulders back and down, letting arms rest naturally by your sides.',
            'Keep spine long, gaze softly forward, and breathe smoothly.'
        ],
        benefits: 'Improves posture, strengthens thighs and ankles, firms abdomen and buttocks.'
    },
    urdhva_hastasana: {
        icon: 'arrows-alt-v',
        categoryTag: 'Upward Stretch',
        accentColor: '#059669',
        instructions: [
            'From Mountain Pose, inhale and sweep arms out and overhead.',
            'Keep arms parallel or bring palms together without crunching shoulders.',
            'Root down through feet while reaching fingertips toward the ceiling.',
            'Gaze upward toward thumbs while keeping neck comfortable.'
        ],
        benefits: 'Stretches the belly, opens chest and shoulders, relieves mild fatigue.'
    },
    uttanasana: {
        icon: 'level-down-alt',
        categoryTag: 'Forward Fold',
        accentColor: '#047857',
        instructions: [
            'Hinge forward from hips, leading with your chest, not rounding the lower back.',
            'Keep knees softly bent if hamstrings feel tight.',
            'Place hands on floor, ankles, or shins.',
            'Relax head and neck completely toward the mat.'
        ],
        benefits: 'Calms the nervous system, stretches hamstrings, calves, and hips.'
    },
    virabhadrasana_i: {
        icon: 'hiking',
        categoryTag: 'Warrior Flow',
        accentColor: '#2563EB',
        instructions: [
            'Step one foot back 3 to 4 feet, angling back foot at 45 degrees.',
            'Bend front knee directly over front ankle aiming for a 90° angle.',
            'Square hips forward toward the front of your mat.',
            'Raise arms vertically overhead, palms facing each other.',
            'Keep back leg active and press firmly into back heel.'
        ],
        benefits: 'Strengthens shoulders, arms, legs, and back muscles. Expands lungs and chest.'
    },
    virabhadrasana_ii: {
        icon: 'child',
        categoryTag: 'Warrior Flow',
        accentColor: '#3B82F6',
        instructions: [
            'Step feet wide apart. Turn front foot forward and back foot parallel to mat edge.',
            'Bend front knee to 90 degrees directly above front ankle.',
            'Extend arms parallel to the floor, reaching actively through both fingertips.',
            'Gaze steadily over front middle finger with shoulders relaxed.'
        ],
        benefits: 'Increases stamina, tones abdominal organs, relieves backache in second trimester.'
    },
    virabhadrasana_iii: {
        icon: 'plane',
        categoryTag: 'Balance Flow',
        accentColor: '#1D4ED8',
        instructions: [
            'From Warrior I, shift weight onto front standing leg.',
            'Hinge forward at hip, lifting back leg parallel to the floor.',
            'Extend arms straight forward or along torso in line with back leg.',
            'Flex back foot with toes pointing down to square hips to the mat.'
        ],
        benefits: 'Develops full-body balance, strengthens ankles, legs, shoulders, and back.'
    },
    vrikshasana: {
        icon: 'tree',
        categoryTag: 'Balance',
        accentColor: '#10B981',
        instructions: [
            'Shift weight onto one standing foot, rooting into all four corners.',
            'Place sole of opposite foot onto inner calf or inner thigh (never on knee joint).',
            'Bring hands to prayer at heart center or extend overhead like tree branches.',
            'Find a steady gaze point (Drishti) at eye level to hold balance.'
        ],
        benefits: 'Strengthens thighs, calves, ankles, and spine. Enhances neuromuscular focus.'
    },
    utkatasana: {
        icon: 'chair',
        categoryTag: 'Strength',
        accentColor: '#D97706',
        instructions: [
            'Stand in Mountain Pose, inhale and raise arms overhead.',
            'Exhale and bend knees, sitting hips back as if into an imaginary chair.',
            'Keep weight centered in heels; knees should not creep far past toes.',
            'Draw lower belly in to support the lumbar spine.'
        ],
        benefits: 'Strengthens ankles, calves, and thighs. Stimulates heart and diaphragm.'
    },
    garudasana: {
        icon: 'dove',
        categoryTag: 'Balance',
        accentColor: '#7C3AED',
        instructions: [
            'Bend knees slightly and lift right leg to cross thigh over left thigh.',
            'Hook right foot behind left calf if flexibility allows.',
            'Cross left arm over right at elbows, wrapping forearms and pressing palms.',
            'Lift elbows to shoulder height while sinking hips down.'
        ],
        benefits: 'Improves balance, opens shoulder blades and sacrum, strengthens calves.'
    },
    natarajasana: {
        icon: 'skating',
        categoryTag: 'Balance & Backbend',
        accentColor: '#EC4899',
        instructions: [
            'Shift weight onto left foot. Bend right knee and grasp inner right ankle with right hand.',
            'Inhale and reach left arm forward and upward.',
            'Hinge forward slightly while kicking right foot back and up away from body.',
            'Keep hips level and chest lifted.'
        ],
        benefits: 'Stretches shoulders, chest, thighs, and groin. Develops elegance and poise.'
    },
    trikonasana: {
        icon: 'shapes',
        categoryTag: 'Standing',
        accentColor: '#0284C7',
        instructions: [
            'Step feet wide apart. Turn right foot 90 degrees out, left foot slightly in.',
            'Extend arms wide at shoulder height.',
            'Reach torso forward over right leg, then hinge down placing right hand on shin or floor.',
            'Extend left arm straight up toward the ceiling in one vertical line.'
        ],
        benefits: 'Stretches and strengthens thighs, knees, and ankles. Stimulates abdominal organs.'
    },
    parsvakonasana: {
        icon: 'running',
        categoryTag: 'Side Angle',
        accentColor: '#0EA5E9',
        instructions: [
            'From Warrior II, rest front forearm on front thigh or place hand on floor outside foot.',
            'Sweep top arm up and forward over ear in a diagonal line from back heel to fingertips.',
            'Roll top ribs open toward the ceiling.',
            'Keep front knee at 90 degrees.'
        ],
        benefits: 'Strengthens legs and ankles, stretches groin, spine, waist, and lungs.'
    },
    adho_mukha_svanasana: {
        icon: 'dog',
        categoryTag: 'Inversion',
        accentColor: '#6366F1',
        instructions: [
            'Start on hands and knees with hands shoulder-width and knees hip-width.',
            'Tuck toes, lift knees off floor, and press hips high toward ceiling creating an inverted V.',
            'Press evenly through palms, lengthening through spine and tailbone.',
            'Pedal feet gently and draw heels toward floor.'
        ],
        benefits: 'Full body rejuvenation, lengthens hamstrings and spine, relieves back pain.'
    },
    phalakasana: {
        icon: 'minus',
        categoryTag: 'Core',
        accentColor: '#DC2626',
        instructions: [
            'Plant hands directly under shoulders with fingers spread wide.',
            'Step feet back, engaging core, quadriceps, and glutes.',
            'Maintain a straight, unbroken diagonal line from head to heels.',
            'Keep neck neutral, looking slightly ahead of fingertips.'
        ],
        benefits: 'Builds core strength, strengthens wrists, shoulders, and spine.'
    },
    chaturanga_dandasana: {
        icon: 'align-justify',
        categoryTag: 'Upper Body',
        accentColor: '#B91C1C',
        instructions: [
            'From Plank Pose, shift weight slightly forward on toes.',
            'Lower torso down, bending elbows back close to ribcage at a 90° angle.',
            'Keep body in a rigid straight line without letting hips sag.',
            'Shoulders should remain at or above elbow height.'
        ],
        benefits: 'Develops arm, wrist, and shoulder stability. Tones abdominal muscles.'
    },
    bhujangasana: {
        icon: 'infinity',
        categoryTag: 'Backbend',
        accentColor: '#D97706',
        instructions: [
            'Lie prone on stomach with tops of feet pressing into floor.',
            'Place hands under shoulders, hugging elbows close to sides.',
            'Inhale and gently peel chest off floor using back muscles rather than arm force.',
            'Keep shoulders relaxed away from ears.'
        ],
        benefits: 'Strengthens spine, opens heart and lungs, firms buttocks.'
    },
    urdhva_mukha_svanasana: {
        icon: 'sun',
        categoryTag: 'Backbend',
        accentColor: '#EA580C',
        instructions: [
            'From Chaturanga, roll over toes onto tops of feet.',
            'Straighten arms, lifting chest, thighs, and knees completely off the floor.',
            'Draw shoulders back and open collarbones wide.',
            'Keep gaze forward or gently lifted.'
        ],
        benefits: 'Improves posture, strengthens spine, arms, and wrists. Stimulates abdominal organs.'
    },
    balasana: {
        icon: 'feather',
        categoryTag: 'Restorative',
        accentColor: '#10B981',
        instructions: [
            'Kneel on floor with big toes touching and knees wide.',
            'Sit hips back onto heels and fold torso forward between thighs.',
            'Rest forehead comfortably on the mat.',
            'Extend arms forward or rest them alongside body palms up.'
        ],
        benefits: 'Calms mind, releases tension in back, shoulders, and neck. Deep relaxation.'
    },
    setu_bandhasana: {
        icon: 'archway',
        categoryTag: 'Backbend',
        accentColor: '#8B5CF6',
        instructions: [
            'Lie on back with knees bent and feet flat on floor, hip-width apart.',
            'Keep arms alongside body, palms pressing down.',
            'Press feet and arms down to lift hips toward ceiling.',
            'Interlace fingers under pelvis if accessible, rolling shoulders underneath.'
        ],
        benefits: 'Stretches chest, neck, and spine. Calms brain and rejuvenates tired legs.'
    },
    paschimottanasana: {
        icon: 'compress-arrows-alt',
        categoryTag: 'Seated',
        accentColor: '#059669',
        instructions: [
            'Sit with legs extended straight forward and spine tall.',
            'Inhale, raise arms overhead to lengthen spine.',
            'Exhale and hinge forward from hips, reaching hands toward shins, ankles, or feet.',
            'Keep spine long, folding belly toward thighs.'
        ],
        benefits: 'Calms brain, relieves stress, stretches spine, shoulders, and hamstrings.'
    },
    baddha_konasana: {
        icon: 'gem',
        categoryTag: 'Hip Opener',
        accentColor: '#10B981',
        instructions: [
            'Sit tall and bend knees, bringing soles of feet together.',
            'Let knees open out to the sides toward the floor.',
            'Hold feet with hands, lengthening up through crown of head.',
            'Gently fold forward from hips if comfortable.'
        ],
        benefits: 'Stimulates heart, improves circulation, stretches inner thighs, groins, and knees.'
    },
    navasana: {
        icon: 'ship',
        categoryTag: 'Core',
        accentColor: '#EF4444',
        instructions: [
            'Sit with knees bent, feet flat on floor. Lean torso back slightly.',
            'Lift feet off floor with shins parallel to ground (or straighten legs into a V shape).',
            'Reach arms forward parallel to the floor alongside legs.',
            'Keep chest lifted and avoid rounding lower back.'
        ],
        benefits: 'Tones and strengthens abdominal muscles, hip flexors, and spine.'
    },
    bakasana: {
        icon: 'feather-alt',
        categoryTag: 'Arm Balance',
        accentColor: '#8B5CF6',
        instructions: [
            'Squat down with feet together and plant palms flat on floor, shoulder-width.',
            'Lift hips high and place knees high on backs of upper arms/triceps.',
            'Shift weight forward into hands, looking slightly ahead.',
            'Lift one foot, then the other, balancing completely on hands.'
        ],
        benefits: 'Strengthens wrists, arms, and abdomen. Develops intense mental concentration.'
    },
    kapotasana: {
        icon: 'crow',
        categoryTag: 'Hip Opener',
        accentColor: '#F59E0B',
        instructions: [
            'From Down Dog, bring right knee forward behind right wrist.',
            'Slide left leg straight back with top of foot flat on mat.',
            'Square hips forward. Inhale and lengthen spine.',
            'Exhale and fold forward over right shin, resting forehead on hands or mat.'
        ],
        benefits: 'Deep external hip rotation, releases stored emotional stress, stretches glutes.'
    },
    matsyasana: {
        icon: 'fish',
        categoryTag: 'Heart Opener',
        accentColor: '#06B6D4',
        instructions: [
            'Lie on back with legs straight and feet together.',
            'Slide hands under buttocks with palms down.',
            'Press forearms and elbows into floor, lifting chest toward ceiling.',
            'Tilt head back gently until crown rests lightly on the floor.'
        ],
        benefits: 'Expands ribcage and lungs, stretches throat and chest, relieves spinal stiffness.'
    },
    dhanurasana: {
        icon: 'circle-notch',
        categoryTag: 'Backbend',
        accentColor: '#F97316',
        instructions: [
            'Lie on belly, bend knees, and reach back to grasp outer ankles.',
            'Inhale and kick feet back into hands, lifting chest and thighs off the floor.',
            'Look forward or slightly up, balancing weight on abdomen.',
            'Breathe evenly throughout the hold.'
        ],
        benefits: 'Strengthens back muscles, improves posture, stimulates abdominal organs.'
    },
    marjaryasana: {
        icon: 'cat',
        categoryTag: 'Spine Mobility',
        accentColor: '#10B981',
        instructions: [
            'Start in tabletop on hands and knees with neutral spine.',
            'Exhale, press hands into floor, and round spine toward ceiling like an angry cat.',
            'Tuck tailbone and gently drop head toward chest.',
            'Inhale to transition into Cow Pose.'
        ],
        benefits: 'Improves spinal flexibility, releases tension in back and neck.'
    },
    bitilasana: {
        icon: 'paw',
        categoryTag: 'Spine Mobility',
        accentColor: '#059669',
        instructions: [
            'Start in tabletop on hands and knees.',
            'Inhale, drop belly toward mat, and lift chest and tailbone toward ceiling.',
            'Draw shoulders away from ears and gaze gently upward.',
            'Exhale to transition back into Cat Pose.'
        ],
        benefits: 'Massages spine and internal organs, relieves stress and back fatigue.'
    },
    ardha_matsyendrasana: {
        icon: 'sync',
        categoryTag: 'Spinal Twist',
        accentColor: '#6366F1',
        instructions: [
            'Sit with legs extended. Bend right knee and place right foot outside left thigh.',
            'Bend left knee, tucking left foot near right hip.',
            'Place right hand behind hip on floor for support.',
            'Inhale to lengthen spine; exhale and twist torso to the right, hooking left elbow outside right knee.'
        ],
        benefits: 'Detoxifies internal organs, promotes spinal mobility, relieves neck stiffness.'
    },
    shavasana: {
        icon: 'bed',
        categoryTag: 'Integration',
        accentColor: '#64748B',
        instructions: [
            'Lie flat on back with legs extended comfortably wide.',
            'Let feet flop open naturally to the sides.',
            'Rest arms alongside torso with palms facing up.',
            'Close eyes, release control of breath, and relax every muscle completely.'
        ],
        benefits: 'Integrates practice benefits, reduces blood pressure and anxiety, calms nervous system.'
    },
    malasana: {
        icon: 'child',
        categoryTag: 'Hip Opener',
        accentColor: '#10B981',
        instructions: [
            'Squat low with feet slightly wider than hips, toes angled outward.',
            'Bring palms together at heart center, pressing elbows into inner knees.',
            'Keep spine long and tailbone heavy toward the ground.',
            'Breathe steadily into the pelvic floor and hips.'
        ],
        benefits: 'Releases lower back tension, increases ankle mobility, tones pelvic muscles.'
    },
    ananda_balasana: {
        icon: 'smile',
        categoryTag: 'Restorative',
        accentColor: '#06B6D4',
        instructions: [
            'Lie on back and draw knees toward armpits.',
            'Grip outer edges of feet with hands, flexing feet soles toward ceiling.',
            'Gently draw knees toward the mat while keeping sacrum grounded.',
            'Rock gently side to side to massage the lower spine.'
        ],
        benefits: 'Gently stretches inner groins and spine, calms brain, relieves fatigue.'
    },
    eka_pada_rajakapotasana: {
        icon: 'feather',
        categoryTag: 'Hip Opener',
        accentColor: '#F59E0B',
        instructions: [
            'Bring front shin forward behind wrists, extending back leg straight behind.',
            'Square hips toward the front edge of the mat.',
            'Lengthen spine upward before folding forward over front leg if comfortable.',
            'Rest forehead on mat or stacked hands and breathe into outer hip.'
        ],
        benefits: 'Deeply stretches glutes, piriformis, and psoas; releases stored physical tension.'
    },
    ardha_chandrasana: {
        icon: 'moon',
        categoryTag: 'Balance Flow',
        accentColor: '#3B82F6',
        instructions: [
            'Shift weight onto front standing foot, placing fingertips on floor or block ahead.',
            'Lift back leg parallel to floor, flexing back foot firmly.',
            'Revolve top hip and shoulder open toward ceiling.',
            'Extend top arm straight up, steadying gaze.'
        ],
        benefits: 'Strengthens ankles, thighs, and abdomen; improves coordination and balance.'
    },
    chakrasana: {
        icon: 'circle-notch',
        categoryTag: 'Peak Backbend',
        accentColor: '#EF4444',
        instructions: [
            'Lie on back with knees bent, feet flat, and hands planted beside ears fingers pointing to shoulders.',
            'Press through palms and feet to press chest and hips high toward ceiling.',
            'Straighten arms and roll inner thighs down.',
            'Breathe smoothly, lowering gently down onto upper back to release.'
        ],
        benefits: 'Strengthens arms, wrists, legs, and spine; stimulates thyroid and pituitary glands.'
    },
    ustrasana: {
        icon: 'fire',
        categoryTag: 'Heart Opener',
        accentColor: '#D97706',
        instructions: [
            'Kneel with hips stacked over knees, pressing shins firmly into mat.',
            'Place hands on lower back, lifting chest upward to begin arch.',
            'Reach hands back to grasp heels if accessible.',
            'Keep hips pressing forward over knees and neck comfortable.'
        ],
        benefits: 'Opens front body, expands lungs and ribcage, strengthens back extensors.'
    },
    sarvangasana: {
        icon: 'arrows-alt-v',
        categoryTag: 'Inversion',
        accentColor: '#8B5CF6',
        instructions: [
            'From back, lift legs and hips overhead, supporting mid-back with hands.',
            'Walk hands up back toward shoulder blades, reaching legs vertically.',
            'Keep neck still and gaze toward toes.',
            'Breathe slowly through diaphragm.'
        ],
        benefits: 'Stimulates thyroid gland, improves venous circulation, calms nervous system.'
    },
    sirsasana_prep: {
        icon: 'shield-alt',
        categoryTag: 'Inversion Prep',
        accentColor: '#6366F1',
        instructions: [
            'Plant forearms parallel on mat, elbows shoulder-distance apart.',
            'Tuck toes and lift hips high into Dolphin stance.',
            'Press forearms down firmly to draw chest toward thighs.',
            'Maintain steady breathing while building shoulder stability.'
        ],
        benefits: 'Builds core and shoulder girdle strength, prepares body for full inversions.'
    }
};

/**
 * Returns metadata (icon, instructions, benefits) for any pose ID
 */
export function getPoseMetadata(poseId) {
    if (!poseId) return null;
    const cleanId = poseId.toLowerCase().trim();
    return POSE_METADATA[cleanId] || {
        icon: 'spa',
        categoryTag: 'Asana Practice',
        accentColor: '#1B4D3E',
        instructions: [
            'Position yourself in full view of the camera.',
            'Follow the on-screen skeleton guidance to match the target posture.',
            'Hold steadily once your joints lock into the green target range.'
        ],
        benefits: 'Enhances body awareness, flexibility, and physical alignment.'
    };
}
