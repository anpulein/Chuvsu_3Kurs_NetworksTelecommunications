// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// // Write your JavaScript code.
// $(function(){
//     $(".chat").niceC();
// }) 

document.getElementById('file-upload').addEventListener('change', function() {
    this.parentNode.parentNode.dispatchEvent(new Event('submit'));
});