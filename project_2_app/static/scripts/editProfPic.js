console.log('editProfPic.js is linked')

// $(`.edit-prof-pic`).on('click', () => {
//     $(`.prof-pic-section`).empty();
//     $(`.prof-pic-section`).append(`
//         <p>Update your profile picture</p>
//         <form method="post" class="profile-pic-form">
//             <p>
//                 <label for="id_image_link">Image link:</label> 
//                 <textarea name="image_link" cols="40" rows="10" required="" id="id_image_link"></textarea>
//             </p>
//             <button type="submit" class="update-pic">Save</button>
//         </form>
//     `);

//     $(`.update-pic`).on('click', () => {
//         const newPic = $(`textarea`).val()
//         console.log(newPic)
//         $.ajax({
//             method: 'POST',
//             url: $(`.prof-pic-section`).attr('data-prof-edit'),
//             data: {'newPic': newPic},
//             success: console.log("success"),
//             error: err => console.log("error >>>>>> ", err)
//         });
//     });
// });