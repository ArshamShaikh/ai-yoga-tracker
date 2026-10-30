const fs = require('fs');
const path = require('path');
const apiPoses = require('./yoga_api_poses.json');
const ourPoses = require('./src/constants/poseConstraints.json').yoga_poses;

const targetDir = path.join(__dirname, 'assets', 'poses');
if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
}

// 1:1 map for each pose in our taxonomy
const POSE_ID_TO_API_ID = {
    'tadasana': 41,
    'urdhva_hastasana': 39,
    'uttanasana': 38,
    'ardha_uttanasana': 38,
    'phalakasana': 26,
    'chaturanga_dandasana': 26,
    'bhujangasana': 35,
    'urdhva_mukha_svanasana': 43,
    'adho_mukha_svanasana': 15,
    'virabhadrasana_i': 44,
    'virabhadrasana_ii': 45,
    'virabhadrasana_iii': 46,
    'trikonasana': 42,
    'parsvakonasana': 18,
    'vrikshasana': 41,
    'utkatasana': 9,
    'ashta_chandrasana': 12,
    'garudasana': 16,
    'natarajasana': 17,
    'navasana': 1,
    'vasisthasana': 34,
    'ardha_pincha_mayurasana': 14,
    'bakasana': 13,
    'paschimottanasana': 30,
    'baddhakonasana': 5,
    'kapotasana': 24,
    'ardha_matsyendrasana': 32,
    'setu_bandhasana': 4,
    'balasana': 10,
    'savasana': 11,
    'shalabhasana': 35,
    'janu_sirsasana': 30,
    'dhanurasana': 3,
    'marjaryasana': 7,
    'bitilasana': 8,
    'matsyasana': 4
};

async function downloadAll() {
    console.log(`Starting download for all taxonomy poses...`);

    for (const pose of ourPoses) {
        const poseId = pose.id;
        const apiId = POSE_ID_TO_API_ID[poseId] || 41;
        const item = apiPoses.find(p => p.id === apiId);
        if (!item || !item.url_png) {
            console.warn(`No PNG for ${poseId}`);
            continue;
        }

        const filePath = path.join(targetDir, `${poseId}.png`);
        try {
            const res = await fetch(item.url_png);
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            const buffer = Buffer.from(await res.arrayBuffer());
            fs.writeFileSync(filePath, buffer);
            console.log(`✓ Saved ${poseId}.png`);
        } catch (err) {
            console.error(`✗ Error downloading ${poseId}:`, err.message);
        }
    }

    console.log('Finished downloading all pose figures!');
}

downloadAll();
