document.addEventListener('DOMContentLoaded', function() {
    const countDisplay = document.getElementById('count');
    const clickBtn = document.getElementById('click-btn');
    const toastContainer = document.getElementById('toast-container');

    function showToast(message, type) {
        const toast = document.createElement('div');
        toast.className = 'toast ' + type;
        toast.textContent = message;
        toastContainer.appendChild(toast);
        // Trigger reflow for CSS transition
        toast.offsetHeight;
        toast.classList.add('show');
        // Remove after 3 seconds
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => {
                toast.remove();
            }, 300);
        }, 3000);
    }

    clickBtn.addEventListener('click', function() {
        fetch('/increment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            countDisplay.textContent = data.count;
            showToast('Counter updated to ' + data.count, 'success');
        })
        .catch(error => {
            console.error('Error:', error);
            showToast('Failed to update counter', 'error');
        });
    });
});
