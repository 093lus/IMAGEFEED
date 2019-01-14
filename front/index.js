         var page = 1, count = 5
        window.onscroll = scrollFunction;
        function scrollFunction() {
            if (document.body.clientHeight + document.body.scrollTop >= document.body.scrollHeight) {
                setTimeout(function () {
                    performLoad();
                }, 1000);
            }
        }

        function changeLike(e){
           var id=$(e.target).attr('id');
           id=id.substring(3,id.length);

            $.ajax({
                 type: 'PUT',
                 url: 'http://localhost:8000/api/feed/',
                 data: {id: id},
                 success: function (data) {  $(e.target).html($(e.target).html()=='Unlike'?'Like':'Unlike'); },
             });



        }

        function appendItem(item){
            $('.wrapper').append(

                        "<div class='box'>" + item.title + "  <br> <img width=160px src='" + 'http://localhost:8000' + item.image +
                            "'alt='Italian Trulli'>  <button style='margin-left:30%' onclick='changeLike(event)' id='img"+item.id+"'>"+(item.status?"Unlike":"Like")+"</button> <br> <br>" + item.description + "</div>"
                    )
        }

        function performLoad() {

            var jqxhr = $.getJSON("http://localhost:8000/api/feed/?page=" + page , function (data) {
                data.map(x => {
                  appendItem(x);
                })
            })
                .done(function () {

                })
                .fail(function () {

                })
                .always(function () {
                    page++;
                });
        };

        $(document).ready(function () {

            performLoad()
        })

        $('#submitNewImage').click(function (event) {
        var form = document.querySelector('form');
    var formData = new FormData(form);
     var other_data = $('form').serializeArray();
      $.each(other_data,function(key,input){
        formData.append(input.name,input.value);
    });

            $.ajax({
                type: 'POST',
                url: 'http://localhost:8000/api/feed/',
                data: formData,
                success: function (data) { appendItem(data) },
//                contentType: "multipart/form-data; boundary=63c5979328c44e2c869349443a94200e ",
                processData: false,
                contentType: false,
            });
        })

