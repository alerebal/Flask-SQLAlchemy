document.addEventListener('DOMContentLoaded', function () {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
    // modal delete_category
    let elems = document.querySelectorAll('.modal');
    M.Modal.init(elems);
});
