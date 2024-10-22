function submitRating(ratingName) {
    const ratings = document.getElementsByName(ratingName);
    let ratingValue;
    for (let rating of ratings) {
        if (rating.checked) {
            ratingValue = rating.value;
        }
    }
    if (ratingValue) {
        alert(`Você avaliou este pintor com ${ratingValue} estrelas!`);
        // Enviar a avaliação para o backend ou atualizar a avaliação média
        updateAverageRating(ratingName, ratingValue);
    } else {
        alert('Por favor, selecione uma avaliação.');
    }
}

function updateAverageRating(ratingName, newRating) {
    // Simular atualização da média de avaliações (aqui você pode conectar com o backend)
    const averageRatingElement = document.getElementById('average-rating' + ratingName.replace('rating', ''));
    averageRatingElement.textContent = newRating; // Apenas substituindo por simplicidade
}
