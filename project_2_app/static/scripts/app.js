$(`.invite-form`).on('submit', (event) => {
    event.preventDefault();
    let checkedContacts = [];
    $(`input[name='contact']:checked`).each((index, contact) => {
        checkedContacts.push($(contact).val())
    });

    $.ajax({
        method: 'POST',
        url: $(`.invite-form`).attr('data-invite-url'),
        data: {'checkedContacts': checkedContacts},
        success: console.log("Success"),
        error: err => console.log(err)
    });
});

$(`.confirmation`).on('click', () => {
    $.ajax({
        method: 'POST',
        url: $(`.confirmation`).attr('data-event-detail-url'),
        data: {'confirmation': true},
        success: console.log("Success"),
        error: err => console.log("err >>>>", err)
    });
});

// when button is clicked, send post request
// if invitation confirmation = true, do not show button on page