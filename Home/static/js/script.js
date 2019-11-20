$(function(){
    //click button to show/hide content
    var button = true;
    $('#btnfirst').on('click', function(){
        if ($('#btnfirst').text().indexOf('Đóng') > -1){
        $(this).text('Chọn chỗ');
        } else{
        $(this).text('Đóng');
        }
    });
    // $('#btnsecond').on('click', function(){
    //     if ($('#btnsecond').text().indexOf('Ẩn') > -1){
    //     $(this).text('Chọn chỗ');
    //     } else{
    //     $(this).text('Ẩn');
    //     }
    // });
})