var updateBtns = document.getElementsByClassName('make-appointment')

for(var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var doctorId = this.dataset.doctor
        var action = this.dataset.action
        console.log('DoctorId: ', doctorId, 'Action: ', action)

        console.log('USER: ', user)
        if(user === 'AnonymousUser') {
            console.log('Not logged in')
        }
        else {
            update_user_appointment(doctorId, action)
        }
    })
}

function update_user_appointment(doctorId, action) {
    console.log('User is logged in. Sending data...')

    var url = '/payment/update_appointment/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'doctorId': doctorId, 'action': action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data: ', data)
        location.reload()
    })
}