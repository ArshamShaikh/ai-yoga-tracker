/**
 * poseImages.js
 * Static mapping of local transparent 3D human pose illustrations
 * to allow instant, offline, high-speed rendering in React Native.
 */

export const POSE_IMAGES = {
    'tadasana': require('../../assets/poses/tadasana.png'),
    'urdhva_hastasana': require('../../assets/poses/urdhva_hastasana.png'),
    'uttanasana': require('../../assets/poses/uttanasana.png'),
    'ardha_uttanasana': require('../../assets/poses/ardha_uttanasana.png'),
    'phalakasana': require('../../assets/poses/phalakasana.png'),
    'chaturanga_dandasana': require('../../assets/poses/chaturanga_dandasana.png'),
    'bhujangasana': require('../../assets/poses/bhujangasana.png'),
    'urdhva_mukha_svanasana': require('../../assets/poses/urdhva_mukha_svanasana.png'),
    'adho_mukha_svanasana': require('../../assets/poses/adho_mukha_svanasana.png'),
    'virabhadrasana_i': require('../../assets/poses/virabhadrasana_i.png'),
    'virabhadrasana_ii': require('../../assets/poses/virabhadrasana_ii.png'),
    'virabhadrasana_iii': require('../../assets/poses/virabhadrasana_iii.png'),
    'trikonasana': require('../../assets/poses/trikonasana.png'),
    'parsvakonasana': require('../../assets/poses/parsvakonasana.png'),
    'vrikshasana': require('../../assets/poses/vrikshasana.png'),
    'utkatasana': require('../../assets/poses/utkatasana.png'),
    'ashta_chandrasana': require('../../assets/poses/ashta_chandrasana.png'),
    'garudasana': require('../../assets/poses/garudasana.png'),
    'natarajasana': require('../../assets/poses/natarajasana.png'),
    'navasana': require('../../assets/poses/navasana.png'),
    'vasisthasana': require('../../assets/poses/vasisthasana.png'),
    'ardha_pincha_mayurasana': require('../../assets/poses/ardha_pincha_mayurasana.png'),
    'bakasana': require('../../assets/poses/bakasana.png'),
    'paschimottanasana': require('../../assets/poses/paschimottanasana.png'),
    'baddhakonasana': require('../../assets/poses/baddhakonasana.png'),
    'baddha_konasana': require('../../assets/poses/baddhakonasana.png'),
    'kapotasana': require('../../assets/poses/kapotasana.png'),
    'ardha_matsyendrasana': require('../../assets/poses/ardha_matsyendrasana.png'),
    'setu_bandhasana': require('../../assets/poses/setu_bandhasana.png'),
    'balasana': require('../../assets/poses/balasana.png'),
    'savasana': require('../../assets/poses/savasana.png'),
    'shavasana': require('../../assets/poses/savasana.png'),
    'shalabhasana': require('../../assets/poses/shalabhasana.png'),
    'janu_sirsasana': require('../../assets/poses/janu_sirsasana.png'),
};

export function getPoseImage(poseId) {
    if (!poseId) return null;
    const cleanId = poseId.toLowerCase().trim();
    return POSE_IMAGES[cleanId] || null;
}
