function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        const loginMessage = document.getElementById('login-message');
        if (data.message === 'Login successful') {
            loginMessage.innerHTML = 'Login successful!';
            document.getElementById('login-form').style.display = 'none';
            document.getElementById('product-list').style.display = 'block';
            fetchProducts();
        } else {
            loginMessage.innerHTML = 'Invalid credentials!';
        }
    })
    .catch(error => console.error('Error:', error));
}

function fetchProducts() {
    fetch('/api/products/')
    .then(response => response.json())
    .then(data => {
        const productList = document.getElementById('products');
        data.products.forEach(product => {
            const li = document.createElement('li');
            li.innerHTML = `${product.name} - $${product.price}`;
            productList.appendChild(li);
        });
    })
    .catch(error => console.error('Error:', error));
}
