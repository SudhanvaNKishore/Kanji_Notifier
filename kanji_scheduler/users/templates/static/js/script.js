// const loginText = document.querySelector(".title-text .login");
// const loginForm = document.querySelector("form.login");
// const loginBtn = document.querySelector("label.login");
// const signupBtn = document.querySelector("label.signup");
// const signupLink = document.querySelector("form .signup-link a");

// signupBtn.onclick = () => {
//   loginForm.style.marginLeft = "-50%";
//   loginText.style.marginLeft = "-50%";
// };

// loginBtn.onclick = () => {
//   loginForm.style.marginLeft = "0%";
//   loginText.style.marginLeft = "0%";
// };

// signupLink.onclick = () => {
//   signupBtn.click();
//   return false;
// };

// // Toggle password visibility
// document.querySelectorAll('.toggle-password').forEach(item => {
//   item.addEventListener('click', function() {
//     const input = this.previousElementSibling;
//     if (input.type === "password") {
//       input.type = "text";
//       this.classList.remove('fa-eye');
//       this.classList.add('fa-eye-slash');
//     } else {
//       input.type = "password";
//       this.classList.remove('fa-eye-slash');
//       this.classList.add('fa-eye');
//     }
//   });
// });


// // // // After successful login/signup
// // // window.location.href = "/home/";  // Replace with your new page URL









// // js:
// const loginText = document.querySelector(".title-text .login");
// const loginForm = document.querySelector("form.login");
// const loginBtn = document.querySelector("label.login");
// const signupBtn = document.querySelector("label.signup");
// const signupLink = document.querySelector("form .signup-link a");
// signupBtn.onclick = () => {
//   loginForm.style.marginLeft = "-50%";
//   loginText.style.marginLeft = "-50%";
// };
// loginBtn.onclick = () => {
//   loginForm.style.marginLeft = "0%";
//   loginText.style.marginLeft = "0%";
// };
// signupLink.onclick = () => {
//   signupBtn.click();
//   return false;
// };





// // Select elements
// const loginText = document.querySelector(".title-text .login");
// const loginForm = document.querySelector("form.login");
// const signupForm = document.querySelector("form.signup");
// const loginBtn = document.querySelector("label.login");
// const signupBtn = document.querySelector("label.signup");
// const signupLink = document.querySelector("form .signup-link a");

// // Show the signup form
// signupBtn.onclick = () => {
//     loginForm.style.marginLeft = "-50%";
//     loginText.style.marginLeft = "-50%";
// };

// // Show the login form
// loginBtn.onclick = () => {
//     loginForm.style.marginLeft = "0%";
//     loginText.style.marginLeft = "0%";
// };

// // Handle signup form submission
// if (signupForm) {
//     signupForm.addEventListener('submit', function(event) {
//         event.preventDefault(); // Prevent default form submission

//         const email = signupForm.email.value;
//         const password1 = signupForm.password1.value;
//         const password2 = signupForm.password2.value;

//         // Simple client-side validation
//         if (password1 !== password2) {
//             alert('Passwords do not match!');
//             return;
//         }

//         // AJAX call to submit the form data
//         fetch('/signup/', { // Adjust URL to your signup endpoint
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/x-www-form-urlencoded',
//             },
//             body: new URLSearchParams({
//                 'email': email,
//                 'password1': password1,
//                 'password2': password2,
//             })
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.success) {
//                 alert('Signup successful!');
//                 // Optionally, you can redirect or show a success message
//             } else {
//                 alert(data.message); // Show error messages returned from the server
//             }
//         })
//         .catch(error => {
//             console.error('Error:', error);
//         });
//     });
// }

// // Handle login form submission
// if (loginForm) {
//     loginForm.addEventListener('submit', function(event) {
//         event.preventDefault(); // Prevent default form submission

//         const username = loginForm.username.value;
//         const password = loginForm.password.value;

//         // AJAX call to submit the login data
//         fetch('/login/', { // Adjust URL to your login endpoint
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/x-www-form-urlencoded',
//             },
//             body: new URLSearchParams({
//                 'username': username,
//                 'password': password,
//             })
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.success) {
//                 window.location.href = '/home'; // Redirect to home on successful login
//             } else {
//                 alert(data.message); // Show error messages returned from the server
//             }
//         })
//         .catch(error => {
//             console.error('Error:', error);
//         });
//     });
// }

// // Toggle password visibility
// document.querySelectorAll('.toggle-password').forEach(item => {
//     item.addEventListener('click', function() {
//         const input = this.previousElementSibling;
//         if (input.type === "password") {
//             input.type = "text";
//             this.classList.remove('fa-eye');
//             this.classList.add('fa-eye-slash');
//         } else {
//             input.type = "password";
//             this.classList.remove('fa-eye-slash');
//             this.classList.add('fa-eye');
//         }
//     });
// });

// // Allow clicking on the signup link to switch forms
// signupLink.onclick = () => {
//     signupBtn.click();
//     return false;
// };





// const loginForm = document.querySelector('.login-form');
// const signupForm = document.querySelector('.signup-form');
// const loginRadio = document.getElementById('login');
// const signupRadio = document.getElementById('signup');

// loginRadio.addEventListener('change', () => {
//     if (loginRadio.checked) {
//         signupForm.style.display = 'none';
//         loginForm.style.display = 'block';
//     }
// });

// signupRadio.addEventListener('change', () => {
//     if (signupRadio.checked) {
//         loginForm.style.display = 'none';
//         signupForm.style.display = 'block';
//     }
// });

// // Set initial state
// loginForm.style.display = 'block';
// signupForm.style.display = 'none';



//with toggle feature


//  document.addEventListener('DOMContentLoaded', function() {
//     // Form toggle functionality
//     const loginForm = document.querySelector('form.login');
//     const signupForm = document.querySelector('form.signup');
//     const loginRadio = document.getElementById('login');
//     const signupRadio = document.getElementById('signup');

//     // Toggle between login and signup forms
//     if (loginRadio && signupRadio) {  // Check if elements exist
//         loginRadio.addEventListener('change', () => {
//             if (loginRadio.checked) {
//                 signupForm.style.display = 'none';
//                 loginForm.style.display = 'block';
//             }
//         });

//         signupRadio.addEventListener('change', () => {
//             if (signupRadio.checked) {
//                 loginForm.style.display = 'none';
//                 signupForm.style.display = 'block';
//             }
//         });
//     }

//     // Password toggle functionality
//     const togglePasswordIcons = document.querySelectorAll('.toggle-password');
    
//     togglePasswordIcons.forEach(icon => {
//         icon.addEventListener('click', function(e) {
//             // Prevent the click from submitting the form
//             e.preventDefault();
            
//             // Find the password input field that's a sibling of the icon
//             const passwordField = this.parentElement.querySelector('input[type="password"]');
            
//             if (passwordField) {
//                 // Toggle the password visibility
//                 if (passwordField.type === 'password') {
//                     passwordField.type = 'text';
//                     this.classList.remove('fa-eye');
//                     this.classList.add('fa-eye-slash');
//                 } else {
//                     passwordField.type = 'password';
//                     this.classList.remove('fa-eye-slash');
//                     this.classList.add('fa-eye');
//                 }
//             }
//         });
//     });

//     // Log for debugging
//     console.log('Number of password toggle icons found:', togglePasswordIcons.length);
// });




document.addEventListener('DOMContentLoaded', function() {
    // Form toggle functionality
    const loginForm = document.querySelector('form.login');
    const signupForm = document.querySelector('form.signup');
    const loginRadio = document.getElementById('login');
    const signupRadio = document.getElementById('signup');

    // Toggle between login and signup forms
    if (loginRadio && signupRadio) {
        loginRadio.addEventListener('change', () => {
            if (loginRadio.checked) {
                signupForm.style.display = 'none';
                loginForm.style.display = 'block';
            }
        });

        signupRadio.addEventListener('change', () => {
            if (signupRadio.checked) {
                loginForm.style.display = 'none';
                signupForm.style.display = 'block';
            }
        });
    }

    // Enhanced password toggle functionality
    const togglePasswordIcons = document.querySelectorAll('.toggle-password');
    let isPasswordVisible = false;

    togglePasswordIcons.forEach(icon => {
        icon.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Find the password input within the same parent div
            const passwordInput = this.parentElement.querySelector('input[type="password"], input[type="text"]');
            
            if (passwordInput) {
                // Toggle password visibility state
                isPasswordVisible = !isPasswordVisible;
                
                // Toggle input type and icon
                if (isPasswordVisible) {
                    // Show password
                    passwordInput.type = 'text';
                    this.classList.remove('fa-eye');
                    this.classList.add('fa-eye-slash');
                } else {
                    // Hide password
                    passwordInput.type = 'password';
                    this.classList.remove('fa-eye-slash');
                    this.classList.add('fa-eye');
                }
            }
        });
    });

    // Add hover effect to password toggle icons
    togglePasswordIcons.forEach(icon => {
        icon.style.cursor = 'pointer';
        
        // Optional: Add hover color change
        icon.addEventListener('mouseover', function() {
            this.style.color = '#FF69B4'; // Pink color on hover
        });
        
        icon.addEventListener('mouseout', function() {
            this.style.color = '#999'; // Return to original color
        });
    });
});
