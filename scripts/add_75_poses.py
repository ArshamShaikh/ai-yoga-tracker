import json
import os

new_poses = [
    # --- MILESTONE 2: THERAPY, SPINAL REHAB & DEEP FLEXIBILITY (Poses 31 to 50) ---
    {
        'id': 'marjaryasana',
        'name': 'Cat Pose',
        'sanskrit': 'Marjaryasana',
        'orientation': 'prone',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Spinal Flexion',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_KNEE'],
                'target': {'min': 85, 'max': 105},
                'variance': 15,
                'feedback': {
                    'low': 'Round your spine upward toward the ceiling, tucking tailbone.',
                    'high': 'Draw navel up into spine, spreading shoulder blades wide.'
                }
            },
            {
                'name': 'Arm Verticality',
                'landmarks': ['LEFT_WRIST', 'LEFT_ELBOW', 'LEFT_SHOULDER'],
                'target': {'min': 165, 'max': 180},
                'variance': 12,
                'feedback': {
                    'low': 'Press firmly through palms and straighten arms under shoulders.',
                    'high': 'Keep arms perpendicular to the floor without locking joints.'
                }
            }
        ]
    },
    {
        'id': 'bitilasana',
        'name': 'Cow Pose',
        'sanskrit': 'Bitilasana',
        'orientation': 'prone',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Spinal Extension',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_KNEE'],
                'target': {'min': 85, 'max': 105},
                'variance': 15,
                'feedback': {
                    'low': 'Drop belly toward mat and gently arch your spine.',
                    'high': 'Lift chest and sit bones toward ceiling, gaze softly upward.'
                }
            }
        ]
    },
    {
        'id': 'salamba_bhujangasana',
        'name': 'Sphinx Pose',
        'sanskrit': 'Salamba Bhujangasana',
        'orientation': 'prone',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Elbow 90 Degree Support',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_ELBOW', 'LEFT_WRIST'],
                'target': {'min': 80, 'max': 105},
                'variance': 15,
                'feedback': {
                    'low': 'Plant forearms parallel with elbows directly under shoulders.',
                    'high': 'Keep elbows at right angles supporting chest lift.'
                }
            },
            {
                'name': 'Chest Elevation',
                'landmarks': ['LEFT_EAR', 'LEFT_SHOULDER', 'LEFT_HIP'],
                'target': {'min': 120, 'max': 150},
                'variance': 15,
                'feedback': {
                    'low': 'Press forearms down to draw chest forward through shoulders.',
                    'high': 'Keep shoulders relaxed down away from ears.'
                }
            }
        ]
    },
    {
        'id': 'eka_pada_rajakapotasana',
        'name': 'Pigeon Pose',
        'sanskrit': 'Eka Pada Rajakapotasana',
        'orientation': 'seated',
        'difficulty': 'intermediate',
        'joints': [
            {
                'name': 'Back Leg Extension',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 160, 'max': 180},
                'variance': 15,
                'feedback': {
                    'low': 'Extend back leg straight behind hip, top of foot flat.',
                    'high': 'Keep back thigh rooted and square hips forward.'
                }
            },
            {
                'name': 'Front Knee Deep Fold',
                'landmarks': ['RIGHT_HIP', 'RIGHT_KNEE', 'RIGHT_ANKLE'],
                'target': {'min': 40, 'max': 85},
                'variance': 20,
                'feedback': {
                    'low': 'Keep front knee wider than hip to protect the joint.',
                    'high': 'Square pelvis to front edge of mat without leaning.'
                }
            }
        ]
    },
    {
        'id': 'utthan_pristhasana',
        'name': 'Lizard Pose',
        'sanskrit': 'Utthan Pristhasana',
        'orientation': 'lunge',
        'difficulty': 'intermediate',
        'joints': [
            {
                'name': 'Front Knee Lunge Angle',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 80, 'max': 110},
                'variance': 15,
                'feedback': {
                    'low': 'Keep front foot wide outside hands, knee tracking forward.',
                    'high': 'Sink hips forward and down to stretch hip flexors.'
                }
            },
            {
                'name': 'Back Leg Length',
                'landmarks': ['RIGHT_HIP', 'RIGHT_KNEE', 'RIGHT_ANKLE'],
                'target': {'min': 155, 'max': 180},
                'variance': 15,
                'feedback': {
                    'low': 'Extend back leg long behind you, pressing heel back.',
                    'high': 'Keep back knee soft or lowered gently onto the mat.'
                }
            }
        ]
    },
    {
        'id': 'ardha_hanumanasana',
        'name': 'Half Splits',
        'sanskrit': 'Ardha Hanumanasana',
        'orientation': 'seated',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Front Knee Extension',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 160, 'max': 180},
                'variance': 15,
                'feedback': {
                    'low': 'Straighten front leg, flexing front toes back toward face.',
                    'high': 'Lengthen spine forward over front thigh rather than rounding back.'
                }
            },
            {
                'name': 'Back Knee 90 Degree Angle',
                'landmarks': ['RIGHT_HIP', 'RIGHT_KNEE', 'RIGHT_ANKLE'],
                'target': {'min': 80, 'max': 105},
                'variance': 15,
                'feedback': {
                    'low': 'Stack back hip directly over back knee.',
                    'high': 'Maintain square hips facing front of mat.'
                }
            }
        ]
    },
    {
        'id': 'malasana',
        'name': 'Garland Pose',
        'sanskrit': 'Malasana',
        'orientation': 'standing',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Deep Squat Knee Bend',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 35, 'max': 65},
                'variance': 15,
                'feedback': {
                    'low': 'Squat deep with feet turned out slightly, heels grounded.',
                    'high': 'Lower hips between heels while keeping chest lifted.'
                }
            },
            {
                'name': 'Spine Uprightness',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_KNEE'],
                'target': {'min': 60, 'max': 95},
                'variance': 18,
                'feedback': {
                    'low': 'Press elbows into inner knees to open chest and lengthen spine.',
                    'high': 'Bring palms to heart center in prayer, collarbones wide.'
                }
            }
        ]
    },
    {
        'id': 'supta_matsyendrasana',
        'name': 'Supine Spinal Twist',
        'sanskrit': 'Supta Matsyendrasana',
        'orientation': 'restorative',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Torso-Thigh Rotation',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_KNEE'],
                'target': {'min': 75, 'max': 110},
                'variance': 18,
                'feedback': {
                    'low': 'Drop bent knee across torso while keeping both shoulders grounded.',
                    'high': 'Gaze gently in opposite direction of bent knees.'
                }
            }
        ]
    },
    {
        'id': 'ananda_balasana',
        'name': 'Happy Baby Pose',
        'sanskrit': 'Ananda Balasana',
        'orientation': 'restorative',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Knee 90 Degree Angle',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 75, 'max': 105},
                'variance': 15,
                'feedback': {
                    'low': 'Stack ankles over knees with soles of feet facing ceiling.',
                    'high': 'Gently pull feet downward, drawing knees toward armpits.'
                }
            }
        ]
    },
    {
        'id': 'uttana_shishosana',
        'name': 'Extended Puppy Pose',
        'sanskrit': 'Uttana Shishosana',
        'orientation': 'prone',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Hip Stack over Knee',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_KNEE'],
                'target': {'min': 80, 'max': 105},
                'variance': 15,
                'feedback': {
                    'low': 'Keep hips stacked directly over knees at 90 degrees.',
                    'high': 'Walk hands forward, melting chest and chin toward mat.'
                }
            },
            {
                'name': 'Arm Extension',
                'landmarks': ['LEFT_WRIST', 'LEFT_ELBOW', 'LEFT_SHOULDER'],
                'target': {'min': 160, 'max': 180},
                'variance': 15,
                'feedback': {
                    'low': 'Extend arms long, pressing palms and opening shoulders.',
                    'high': 'Relax forehead or chin onto mat, lengthening spine.'
                }
            }
        ]
    },
    {
        'id': 'parsva_balasana',
        'name': 'Thread the Needle',
        'sanskrit': 'Parsva Balasana',
        'orientation': 'prone',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Arm Cross Rotation',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_ELBOW', 'LEFT_WRIST'],
                'target': {'min': 150, 'max': 180},
                'variance': 18,
                'feedback': {
                    'low': 'Slide arm under chest until shoulder rests comfortably on mat.',
                    'high': 'Rest side of head on mat, feeling gentle twist in upper back.'
                }
            }
        ]
    },
    {
        'id': 'supta_baddha_konasana',
        'name': 'Reclined Bound Angle',
        'sanskrit': 'Supta Baddha Konasana',
        'orientation': 'restorative',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Knee Open Wing Angle',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 35, 'max': 70},
                'variance': 18,
                'feedback': {
                    'low': 'Bring soles of feet together, letting knees fall open to sides.',
                    'high': 'Relax hips and lower belly, breathing deeply.'
                }
            }
        ]
    },
    {
        'id': 'viparita_karani',
        'name': 'Legs-Up-The-Wall',
        'sanskrit': 'Viparita Karani',
        'orientation': 'restorative',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Legs Inverted 90 Degrees',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_ANKLE'],
                'target': {'min': 80, 'max': 105},
                'variance': 15,
                'feedback': {
                    'low': 'Extend legs straight up perpendicular to torso.',
                    'high': 'Rest back of hips flat, relaxing legs and feet completely.'
                }
            }
        ]
    },
    {
        'id': 'anjaneyasana',
        'name': 'Low Lunge',
        'sanskrit': 'Anjaneyasana',
        'orientation': 'lunge',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Front Knee 90 Degree Angle',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 80, 'max': 100},
                'variance': 12,
                'feedback': {
                    'low': 'Step front foot forward until knee stacks over ankle.',
                    'high': 'Lower hips forward and down into front hip flexor.'
                }
            },
            {
                'name': 'Torso Arch',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_KNEE'],
                'target': {'min': 150, 'max': 180},
                'variance': 18,
                'feedback': {
                    'low': 'Sweep arms overhead, lifting ribcage away from pelvis.',
                    'high': 'Gaze gently upward with open heart and relaxed neck.'
                }
            }
        ]
    },
    {
        'id': 'parivrtta_anjaneyasana',
        'name': 'Revolved Low Lunge',
        'sanskrit': 'Parivrtta Anjaneyasana',
        'orientation': 'lunge',
        'difficulty': 'intermediate',
        'joints': [
            {
                'name': 'Front Knee Lunge',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 80, 'max': 105},
                'variance': 15,
                'feedback': {
                    'low': 'Maintain 90-degree bend in front knee.',
                    'high': 'Hook opposite elbow outside front knee into deep twist.'
                }
            }
        ]
    },
    {
        'id': 'parighasana',
        'name': 'Gate Pose',
        'sanskrit': 'Parighasana',
        'orientation': 'standing',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Extended Leg Straightness',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 160, 'max': 180},
                'variance': 15,
                'feedback': {
                    'low': 'Extend one leg straight out to side, toes pointing forward.',
                    'high': 'Reach top arm in long side stretch over ear toward foot.'
                }
            }
        ]
    },
    {
        'id': 'apanasana',
        'name': 'Knees-To-Chest',
        'sanskrit': 'Apanasana',
        'orientation': 'restorative',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Knee Hug Flexion',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 30, 'max': 60},
                'variance': 15,
                'feedback': {
                    'low': 'Hug knees firmly toward chest, relaxing tailbone into floor.',
                    'high': 'Rock gently side to side to massage lumbar spine.'
                }
            }
        ]
    },
    {
        'id': 'prasarita_padottanasana',
        'name': 'Wide-Legged Forward Fold',
        'sanskrit': 'Prasarita Padottanasana',
        'orientation': 'standing',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Legs Straight Fold',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 160, 'max': 180},
                'variance': 12,
                'feedback': {
                    'low': 'Keep legs straight and engage quadriceps.',
                    'high': 'Hinge from hips, walking hands back between feet.'
                }
            },
            {
                'name': 'Torso Forward Hinge',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_KNEE'],
                'target': {'min': 40, 'max': 80},
                'variance': 18,
                'feedback': {
                    'low': 'Lower crown of head toward mat, lengthening spine.',
                    'high': 'Keep weight evenly balanced across outer edges of feet.'
                }
            }
        ]
    },
    {
        'id': 'parsvottanasana',
        'name': 'Pyramid Pose',
        'sanskrit': 'Parsvottanasana',
        'orientation': 'standing',
        'difficulty': 'intermediate',
        'joints': [
            {
                'name': 'Front Leg Straightness',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 160, 'max': 180},
                'variance': 12,
                'feedback': {
                    'low': 'Straighten front knee, drawing front hip back.',
                    'high': 'Fold torso over front thigh with flat spine.'
                }
            }
        ]
    },
    {
        'id': 'ustrasana',
        'name': 'Camel Pose',
        'sanskrit': 'Ustrasana',
        'orientation': 'prone',
        'difficulty': 'intermediate',
        'joints': [
            {
                'name': 'Spinal Backbend Arch',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_KNEE'],
                'target': {'min': 110, 'max': 145},
                'variance': 18,
                'feedback': {
                    'low': 'Lift chest toward ceiling and press hips forward over knees.',
                    'high': 'Reach hands back toward heels while supporting lower back.'
                }
            },
            {
                'name': 'Knee 90 Degree Grounding',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 80, 'max': 105},
                'variance': 15,
                'feedback': {
                    'low': 'Keep thighs perpendicular to the floor.',
                    'high': 'Do not let hips collapse backward toward calves.'
                }
            }
        ]
    },

    # --- MILESTONE 3: POWER, BALANCE, INVERSIONS & PEAK SUITE (Poses 51 to 75) ---
    {
        'id': 'garudasana',
        'name': 'Eagle Pose',
        'sanskrit': 'Garudasana',
        'orientation': 'balance',
        'difficulty': 'intermediate',
        'joints': [
            {
                'name': 'Standing Knee Bend',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 100, 'max': 135},
                'variance': 15,
                'feedback': {
                    'low': 'Sink hips down deeper in chair stance.',
                    'high': 'Wrap thighs tightly, hooking top foot behind calf.'
                }
            },
            {
                'name': 'Elbow Wrap Height',
                'landmarks': ['LEFT_WRIST', 'LEFT_ELBOW', 'LEFT_SHOULDER'],
                'target': {'min': 75, 'max': 105},
                'variance': 18,
                'feedback': {
                    'low': 'Lift crossed elbows up to shoulder level.',
                    'high': 'Press forearms away from face, opening shoulder blades.'
                }
            }
        ]
    },
    {
        'id': 'parivrtta_trikonasana',
        'name': 'Revolved Triangle',
        'sanskrit': 'Parivrtta Trikonasana',
        'orientation': 'standing',
        'difficulty': 'advanced',
        'joints': [
            {
                'name': 'Leg Straightness',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 160, 'max': 180},
                'variance': 12,
                'feedback': {
                    'low': 'Keep both legs straight and grounded.',
                    'high': 'Reach opposite hand to outside of front ankle or floor.'
                }
            },
            {
                'name': 'Arm Vertical Wing Span',
                'landmarks': ['LEFT_WRIST', 'LEFT_SHOULDER', 'RIGHT_WRIST'],
                'target': {'min': 160, 'max': 180},
                'variance': 18,
                'feedback': {
                    'low': 'Extend top arm straight up, stacking shoulders in vertical line.',
                    'high': 'Revolve torso fully toward side wall, gazing up toward thumb.'
                }
            }
        ]
    },
    {
        'id': 'parivrtta_parsvakonasana',
        'name': 'Revolved Side Angle',
        'sanskrit': 'Parivrtta Parsvakonasana',
        'orientation': 'standing',
        'difficulty': 'advanced',
        'joints': [
            {
                'name': 'Front Knee 90 Degree Angle',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 80, 'max': 100},
                'variance': 12,
                'feedback': {
                    'low': 'Maintain 90-degree square bend in front knee.',
                    'high': 'Hook opposite armpit outside front knee into deep rotation.'
                }
            }
        ]
    },
    {
        'id': 'ardha_chandrasana',
        'name': 'Half Moon Pose',
        'sanskrit': 'Ardha Chandrasana',
        'orientation': 'balance',
        'difficulty': 'intermediate',
        'joints': [
            {
                'name': 'Standing Leg Extension',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 160, 'max': 180},
                'variance': 12,
                'feedback': {
                    'low': 'Root down through standing leg, engaging quad.',
                    'high': 'Keep standing foot pointed directly forward.'
                }
            },
            {
                'name': 'Floating Leg Parallel Height',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'RIGHT_ANKLE'],
                'target': {'min': 80, 'max': 105},
                'variance': 15,
                'feedback': {
                    'low': 'Lift floating leg parallel to the floor, foot flexed.',
                    'high': 'Stack top hip directly over bottom hip, opening pelvis.'
                }
            }
        ]
    },
    {
        'id': 'parivrtta_ardha_chandrasana',
        'name': 'Revolved Half Moon',
        'sanskrit': 'Parivrtta Ardha Chandrasana',
        'orientation': 'balance',
        'difficulty': 'advanced',
        'joints': [
            {
                'name': 'Standing Leg Straightness',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 160, 'max': 180},
                'variance': 12,
                'feedback': {
                    'low': 'Lock standing knee softly straight.',
                    'high': 'Revolve torso toward front standing leg while lifting back heel.'
                }
            }
        ]
    },
    {
        'id': 'natarajasana',
        'name': 'Dancer Pose',
        'sanskrit': 'Natarajasana',
        'orientation': 'balance',
        'difficulty': 'advanced',
        'joints': [
            {
                'name': 'Standing Leg Straightness',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 160, 'max': 180},
                'variance': 12,
                'feedback': {
                    'low': 'Keep standing leg strong and straight.',
                    'high': 'Root firmly into all corners of standing foot.'
                }
            },
            {
                'name': 'Lifted Leg Back Extension',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'RIGHT_KNEE'],
                'target': {'min': 120, 'max': 165},
                'variance': 20,
                'feedback': {
                    'low': 'Kick lifted foot back and up into hand, arching back.',
                    'high': 'Reach forward arm long at eye level, lifting chest.'
                }
            }
        ]
    },
    {
        'id': 'chakrasana',
        'name': 'Wheel Pose',
        'sanskrit': 'Urdhva Dhanurasana',
        'orientation': 'prone',
        'difficulty': 'advanced',
        'joints': [
            {
                'name': 'Spinal Arch Elevation',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_KNEE'],
                'target': {'min': 110, 'max': 150},
                'variance': 20,
                'feedback': {
                    'low': 'Press through hands and feet to lift pelvis toward ceiling.',
                    'high': 'Engage glutes and roll inner thighs down.'
                }
            },
            {
                'name': 'Arm Full Extension',
                'landmarks': ['LEFT_WRIST', 'LEFT_ELBOW', 'LEFT_SHOULDER'],
                'target': {'min': 155, 'max': 180},
                'variance': 15,
                'feedback': {
                    'low': 'Straighten arms, pressing floor away through palms.',
                    'high': 'Shift chest forward through upper arms.'
                }
            }
        ]
    },
    {
        'id': 'dhanurasana',
        'name': 'Bow Pose',
        'sanskrit': 'Dhanurasana',
        'orientation': 'prone',
        'difficulty': 'intermediate',
        'joints': [
            {
                'name': 'Knee Kick Lift',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_KNEE'],
                'target': {'min': 140, 'max': 175},
                'variance': 18,
                'feedback': {
                    'low': 'Kick shins strongly back away from torso into hands.',
                    'high': 'Lift chest and thighs off mat, balancing on abdomen.'
                }
            }
        ]
    },
    {
        'id': 'vasisthasana_ii',
        'name': 'Side Plank with Leg Lift',
        'sanskrit': 'Vasisthasana II',
        'orientation': 'balance',
        'difficulty': 'advanced',
        'joints': [
            {
                'name': 'Supporting Arm Line',
                'landmarks': ['LEFT_WRIST', 'LEFT_ELBOW', 'LEFT_SHOULDER'],
                'target': {'min': 165, 'max': 180},
                'variance': 12,
                'feedback': {
                    'low': 'Stack supporting shoulder directly above wrist.',
                    'high': 'Press floor away, keeping side core engaged.'
                }
            },
            {
                'name': 'Leg Abduction Angle',
                'landmarks': ['LEFT_ANKLE', 'LEFT_HIP', 'RIGHT_ANKLE'],
                'target': {'min': 30, 'max': 70},
                'variance': 20,
                'feedback': {
                    'low': 'Lift top leg away from bottom leg, keeping hips high.',
                    'high': 'Reach top arm straight up, gazing toward thumb.'
                }
            }
        ]
    },
    {
        'id': 'camatkarasana',
        'name': 'Wild Thing',
        'sanskrit': 'Camatkarasana',
        'orientation': 'balance',
        'difficulty': 'intermediate',
        'joints': [
            {
                'name': 'Heart Open Backbend',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_KNEE'],
                'target': {'min': 130, 'max': 170},
                'variance': 20,
                'feedback': {
                    'low': 'Press supporting foot down to lift pelvis high.',
                    'high': 'Extend top arm overhead, opening heart to sky.'
                }
            }
        ]
    },
    {
        'id': 'matsyasana',
        'name': 'Fish Pose',
        'sanskrit': 'Matsyasana',
        'orientation': 'restorative',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Thoracic Chest Lift',
                'landmarks': ['LEFT_EAR', 'LEFT_SHOULDER', 'LEFT_HIP'],
                'target': {'min': 120, 'max': 155},
                'variance': 18,
                'feedback': {
                    'low': 'Press forearms down to arch upper back off mat.',
                    'high': 'Rest crown of head lightly on mat without bearing neck weight.'
                }
            }
        ]
    },
    {
        'id': 'gomukhasana',
        'name': 'Cow Face Pose',
        'sanskrit': 'Gomukhasana',
        'orientation': 'seated',
        'difficulty': 'intermediate',
        'joints': [
            {
                'name': 'Knee Stack Angle',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 35, 'max': 65},
                'variance': 15,
                'feedback': {
                    'low': 'Stack knees one directly on top of the other.',
                    'high': 'Sit evenly on both sit bones with spine upright.'
                }
            }
        ]
    },
    {
        'id': 'virasana',
        'name': 'Hero Pose',
        'sanskrit': 'Virasana',
        'orientation': 'seated',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Knee Flexion',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 30, 'max': 55},
                'variance': 15,
                'feedback': {
                    'low': 'Sit between heels on mat or yoga block.',
                    'high': 'Keep spine tall and tops of feet flat against floor.'
                }
            }
        ]
    },
    {
        'id': 'padmasana',
        'name': 'Lotus Pose',
        'sanskrit': 'Padmasana',
        'orientation': 'seated',
        'difficulty': 'advanced',
        'joints': [
            {
                'name': 'Knee External Cross',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 30, 'max': 55},
                'variance': 15,
                'feedback': {
                    'low': 'Place both feet on opposite hip creases soles up.',
                    'high': 'Maintain long vertical spine, hands resting on knees.'
                }
            }
        ]
    },
    {
        'id': 'ardha_padmasana',
        'name': 'Half Lotus Pose',
        'sanskrit': 'Ardha Padmasana',
        'orientation': 'seated',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Knee Cross Fold',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 40, 'max': 70},
                'variance': 15,
                'feedback': {
                    'low': 'Place one foot on opposite thigh, other foot beneath.',
                    'high': 'Rest sit bones grounded with long tall spine.'
                }
            }
        ]
    },
    {
        'id': 'dandasana',
        'name': 'Staff Pose',
        'sanskrit': 'Dandasana',
        'orientation': 'seated',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': '90 Degree L-Shape Torso',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_ANKLE'],
                'target': {'min': 80, 'max': 100},
                'variance': 12,
                'feedback': {
                    'low': 'Sit tall with spine at 90 degrees to extended legs.',
                    'high': 'Flex feet firmly and plant hands flat beside hips.'
                }
            }
        ]
    },
    {
        'id': 'sukhasana',
        'name': 'Easy Pose',
        'sanskrit': 'Sukhasana',
        'orientation': 'seated',
        'difficulty': 'beginner',
        'joints': [
            {
                'name': 'Spine Verticality',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_KNEE'],
                'target': {'min': 80, 'max': 105},
                'variance': 15,
                'feedback': {
                    'low': 'Sit cross-legged comfortably with spine tall.',
                    'high': 'Relax shoulders down, hands resting lightly on knees.'
                }
            }
        ]
    },
    {
        'id': 'sarvangasana',
        'name': 'Shoulderstand',
        'sanskrit': 'Salamba Sarvangasana',
        'orientation': 'inverted_v',
        'difficulty': 'advanced',
        'joints': [
            {
                'name': 'Vertical Body Line',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_ANKLE'],
                'target': {'min': 165, 'max': 180},
                'variance': 12,
                'feedback': {
                    'low': 'Walk hands up back to lift torso vertically.',
                    'high': 'Point toes straight up, keeping weight on shoulders not neck.'
                }
            }
        ]
    },
    {
        'id': 'halasana',
        'name': 'Plow Pose',
        'sanskrit': 'Halasana',
        'orientation': 'inverted_v',
        'difficulty': 'intermediate',
        'joints': [
            {
                'name': 'Hip Flexion Over Head',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_ANKLE'],
                'target': {'min': 50, 'max': 85},
                'variance': 18,
                'feedback': {
                    'low': 'Lower feet to floor beyond head with legs straight.',
                    'high': 'Interlace fingers and press arms flat against mat.'
                }
            }
        ]
    },
    {
        'id': 'sirsasana_prep',
        'name': 'Dolphin Pose',
        'sanskrit': 'Ardha Sirsasana',
        'orientation': 'inverted_v',
        'difficulty': 'intermediate',
        'joints': [
            {
                'name': 'Forearm Support 90 Degrees',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_ELBOW', 'LEFT_WRIST'],
                'target': {'min': 80, 'max': 105},
                'variance': 15,
                'feedback': {
                    'low': 'Plant forearms parallel, elbows shoulder-distance apart.',
                    'high': 'Lift hips high, pressing chest toward thighs.'
                }
            }
        ]
    },
    {
        'id': 'parsva_bakasana',
        'name': 'Side Crow',
        'sanskrit': 'Parsva Bakasana',
        'orientation': 'balance',
        'difficulty': 'advanced',
        'joints': [
            {
                'name': 'Arm Support Bend',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_ELBOW', 'LEFT_WRIST'],
                'target': {'min': 80, 'max': 110},
                'variance': 15,
                'feedback': {
                    'low': 'Bend elbows like Chaturanga to create shelf for thighs.',
                    'high': 'Shift weight into hands, floating both feet off mat.'
                }
            }
        ]
    },
    {
        'id': 'astavakrasana',
        'name': 'Eight-Angle Pose',
        'sanskrit': 'Astavakrasana',
        'orientation': 'balance',
        'difficulty': 'advanced',
        'joints': [
            {
                'name': 'Elbow 90 Degree Angle',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_ELBOW', 'LEFT_WRIST'],
                'target': {'min': 80, 'max': 105},
                'variance': 15,
                'feedback': {
                    'low': 'Bend arms to 90 degrees, locking ankles together.',
                    'high': 'Extend legs straight out to the side parallel to floor.'
                }
            }
        ]
    },
    {
        'id': 'eka_pada_galavasana',
        'name': 'Flying Pigeon',
        'sanskrit': 'Eka Pada Galavasana',
        'orientation': 'balance',
        'difficulty': 'advanced',
        'joints': [
            {
                'name': 'Arm Shelf 90 Degrees',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_ELBOW', 'LEFT_WRIST'],
                'target': {'min': 80, 'max': 105},
                'variance': 15,
                'feedback': {
                    'low': 'Hook front shin high on triceps in 90-degree arm shelf.',
                    'high': 'Extend back leg straight back parallel to the mat.'
                }
            }
        ]
    },
    {
        'id': 'tittibhasana',
        'name': 'Firefly Pose',
        'sanskrit': 'Tittibhasana',
        'orientation': 'balance',
        'difficulty': 'advanced',
        'joints': [
            {
                'name': 'Leg Straight Extension',
                'landmarks': ['LEFT_HIP', 'LEFT_KNEE', 'LEFT_ANKLE'],
                'target': {'min': 155, 'max': 180},
                'variance': 15,
                'feedback': {
                    'low': 'Press thighs into backs of upper arms, extending legs.',
                    'high': 'Flex feet and point toes, lifting chest forward.'
                }
            }
        ]
    },
    {
        'id': 'mayurasana',
        'name': 'Peacock Pose',
        'sanskrit': 'Mayurasana',
        'orientation': 'balance',
        'difficulty': 'advanced',
        'joints': [
            {
                'name': 'Horizontal Body Line',
                'landmarks': ['LEFT_SHOULDER', 'LEFT_HIP', 'LEFT_ANKLE'],
                'target': {'min': 160, 'max': 180},
                'variance': 15,
                'feedback': {
                    'low': 'Plant palms with fingers pointing back, elbows into navel.',
                    'high': 'Shift forward, lifting legs and torso parallel to ground.'
                }
            }
        ]
    }
]

file_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'constants', 'poseConstraints.json')

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_ids = {p['id'] for p in data['yoga_poses']}
added_count = 0

for p in new_poses:
    if p['id'] not in existing_ids:
        data['yoga_poses'].append(p)
        added_count += 1

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

total_count = len(data['yoga_poses'])
print(f'Successfully added {added_count} new poses!')
print(f'Total poses now in poseConstraints.json: {total_count}')
