// script.js
document.querySelectorAll('p a').forEach(link => {
    link.addEventListener('mouseover', function() {
        const topicId = this.getAttribute('data-topic');
        const topicElement = document.getElementById(topicId);
        if (topicElement) {
            topicElement.classList.add('bullet'); // Добавляем класс для изменения стиля
        }
    });

    link.addEventListener('mouseout', function() {
        const topicId = this.getAttribute('data-topic');
        const topicElement = document.getElementById(topicId);
        if (topicElement) {
            topicElement.classList.remove('bullet'); // Удаляем класс при уходе курсора
        }
    });
});
