$(document).ready(function () {
  $('#add_item').click(function () {
    const item = '<li>Item</li>';
    $('UL.my_list').append(item);
  });

  $('#remove_item').click(function () {
    $('UL.my_list li:last').remove();
  });

  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
