         var page = 1, count = 5, backEndURL='http://localhost:8000'
        window.onscroll = scrollFunction;
        function scrollFunction() {
            if (document.body.clientHeight + document.body.scrollTop >= document.body.scrollHeight) {
                performLoad();
            }
        }

        function changeLike(e){
           var id=$(e.target).attr('id');
           id=id.substring(3,id.length);

            $.ajax({
                 type: 'PUT',
                 url: backEndURL+'/api/feed/',
                 data: {id: id},
                 success: function (data) {  $(e.target).html($(e.target).html()=='Unlike'?'Like':'Unlike'); },
             }  );



        }

        function appendItem(item){
            $('.wrapper').append(

                        "<div class='box'>" + item.title + "  <br> <img width=160px src='" + backEndURL + item.image +
                            "'>  <button style='margin-left:30%' onclick='changeLike(event)' id='img"+item.id+"'>"+(item.status?"Unlike":"Like")+"</button> <br> <br>" + item.description + "</div>"
                    )
        }

        function resetForm(){
            $('#title').val('');
            $('#description').val('');
            $('#image').val(null)
        }

        function resetWrapper(){
        $('.wrapper').html('');
        }

        function performLoad() {
            $.getJSON(backEndURL+ "/api/feed/?page=" + page , function (data) {
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

     $('#submitNewImage').click(function (event) {
        var form = document.querySelector('form');
    var formData = new FormData(form);
     var serialized_form = $('form').serializeArray();
      $.each(serialized_form,function(key,input){
        formData.append(input.name,input.value);
    });

            $.ajax({
                type: 'POST',
                url: backEndURL+'/api/feed/',
                data: formData,
                success: function (data) { resetForm(); page=1; resetWrapper(); performLoad() },
                processData: false,
                contentType: false,
            });
        })
        })





