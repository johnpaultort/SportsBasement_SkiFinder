function scoreSki(ski, user) {
    let score = 0;

    // Style
    if (ski.styles.includes(user.style)) {
        score += 30;
    }

    // Terrain
    user.terrain.forEach(t => {
        if (ski.terrain.includes(t)) {
            score += 15;
        }
    });

    // Preference
    user.preferences.forEach(p => {
        if (ski.preferences.includes(p)) {
            score += 10;
        }
    });

    // Skill
    if (ski.skill.includes(user.skill)) {
        score += 20;
    }

    return score;
}