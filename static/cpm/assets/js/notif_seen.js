$('.notification_id').click(function(){
     $.ajax({
          url: "/notification/seen/",
          data: {
               'csrfmiddlewaretoken': '{{ csrf_token }}',
               'notif_id' : $(this).attr('data-id'),
          }
     })
})
