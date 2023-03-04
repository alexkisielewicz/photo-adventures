// Initialize bootstrap modal to allow post deletion
$(document).ready(function () {
    const deleteConfirmationModal = new bootstrap.Modal(document.getElementById('deleteModal'))
    document.querySelector('[data-target="#deleteModal"]').addEventListener('click', () => {
        deleteConfirmationModal.show()
    })

    $('.delete-post-btn').click(function (event) {
        let postId = $(this).data('post-id');
        $('#deleteForm input[name="post_id"]').val(postId);
    });
});