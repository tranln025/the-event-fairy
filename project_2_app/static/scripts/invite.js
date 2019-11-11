// console.log('invite.js is linked')

// $(`.invite-form`).on('submit', (event) => {
//     event.preventDefault();
//     let checkedContacts = [];
//     $(`input[name='contact']:checked`).each((index, contact) => {
//         checkedContacts.push($(contact).val())
//     });
//     console.log(checkedContacts) // array of usernames

//     $.ajax({
//         method: 'POST',
//         url: $(`.invite-form`).attr('data-invite-url'),
//         data: {'checkedContacts': checkedContacts},
//         success: console.log("success"),
//         error: err => console.log("error >>>>>> ", err)
//     });
// });
