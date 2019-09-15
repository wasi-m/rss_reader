$(document).ready(function () {
    console.log("main.js");

    $('#summary_table').DataTable({
        "pagingType": "full_numbers",
        "lengthMenu": [[15, 30, 50, -1], [15, 30, 50, "All"]],
        responsive: true,
        language: {
            search: "_INPUT_",
            searchPlaceholder: "Search feeds",
        }
    });

});