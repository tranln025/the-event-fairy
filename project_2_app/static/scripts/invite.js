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
        success: console.log("success"),
        error: err => console.log(err)
    });
});