$(function (){
$('table tbody th:first-child').each(function (i) {
$(this).html(i+1);
});
});