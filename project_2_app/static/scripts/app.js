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

    setTimeout(function() {
        window.location.href = $(`.invite-form`).attr('data-event-detail-url');
    }, 100);
});

$(`.confirmation`).on('click', () => {
    $.ajax({
        method: 'POST',
        url: $(`.confirmation`).attr('data-event-detail-url'),
        data: {'confirmation': true},
        success: console.log("Success"),
        error: err => console.log("err >>>>", err)
    });

    setTimeout(function() {
        window.location.reload();
    }, 100);

   
});