const clientFirstName = document.getElementById('clientFirstName');
const clientLastName = document.getElementById('clientLastName');
const emailField = document.getElementById('emailField');
const phoneField = document.getElementById('phoneField');
const notesField = document.getElementById('notesField');
const clientID = document.getElementById('clientID');

const fields = [clientFirstName, clientLastName, emailField, phoneField, notesField];

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function saveChanges() {
    const updatedData = {
        clientFirst: clientFirstName.textContent,
        clientLast: clientLastName.textContent,
        email: emailField.textContent,
        phone: phoneField.textContent,
        notes: notesField.textContent
    };

    fetch(`/${clientID.textContent}/updateclientinfo/`, { // Make sure the URL is correct
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ updatedData: updatedData }) // Ensure data structure matches backend expectation
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        toggleEdit();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

let isEditMode = false; // This flag will keep track of the current mode

function toggleEdit() {
    isEditMode = !isEditMode; // Toggle the mode
    const button = document.querySelector('button');
    if (isEditMode) {
        button.textContent = 'Save Changes';
        makeEditable(true);
    } else {
        button.textContent = 'Edit Fields';
        makeEditable(false);
        saveChanges(); // Save changes when exiting edit mode
    }
}

function makeEditable(editable) {
    fields.forEach(field => {
        field.contentEditable = editable;
        field.style.border = editable ? '2px solid black' : 'none';
    });
}

// Bind the event listener once, outside the toggleEdit function
document.querySelector('button').addEventListener('click', toggleEdit);
