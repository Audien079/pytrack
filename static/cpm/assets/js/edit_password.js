function hasLowerCase(str) {
     return (/[a-z]/.test(str));
 }

 function hasUpperCase(str) {
     return (/[A-Z]/.test(str));
 }

 function hasNum(str) {
     return (/[1-9]/.test(str));
 }

 function hasSp(str) {
     return (/[!@#$%*]/.test(str));
 }

 $('input[name="password2"]').keyup(function(){
     var a = $(this).val()
     var b = $('input[name="password1"]').val()
     if (a == b){
         $('input[id="match"]').prop('checked', true)
         $('input[id="match"]').parent().addClass('checkbox-success')
         $('input[id="match"]').parent().removeClass('checkbox-danger')
         if (b.length >= 8){
             $('input[id="min_8"]').prop('checked', true)
             $('input[id="min_8"]').parent().addClass('checkbox-success')
             $('input[id="min_8"]').parent().removeClass('checkbox-danger')
         }else{
             $('input[id="min_8"]').prop('checked', true)
            }
         if (hasLowerCase(b)){
             $('input[id="lower_case"]').prop('checked', true)
             $('input[id="lower_case"]').parent().addClass('checkbox-success')
             $('input[id="lower_case"]').parent().removeClass('checkbox-danger')
         }else{
             $('input[id="lower_case"]').prop('checked', true)
            }
         if (hasUpperCase(b)){
             $('input[id="upper_case"]').prop('checked', true)
             $('input[id="upper_case"]').parent().addClass('checkbox-success')
             $('input[id="upper_case"]').parent().removeClass('checkbox-danger')
         }else{
             $('input[id="upper_case"]').prop('checked', true)
            }
         if (hasNum(b)){
             $('input[id="has_num"]').prop('checked', true)
             $('input[id="has_num"]').parent().addClass('checkbox-success')
             $('input[id="has_num"]').parent().removeClass('checkbox-danger')
         }else{
             $('input[id="has_num"]').prop('checked', true)
            }
         if (hasSp(b)){
             $('input[id="has_sp"]').prop('checked', true)
             $('input[id="has_sp"]').parent().addClass('checkbox-success')
             $('input[id="has_sp"]').parent().removeClass('checkbox-danger')
         }else{
             $('input[id="has_sp"]').prop('checked', true)
            }
         var count = 0
         $('input[name="pass1"]').each(function(){
              if ($(this).parent().hasClass('checkbox-success')){
                   count = count + 1
              }
         })
         if (count > 2){
             $('input[id="min_3"]').prop('checked', true)
             $('input[id="min_3"]').parent().addClass('checkbox-success')
             $('input[id="min_3"]').parent().removeClass('checkbox-danger')
         }else{
             $('input[id="min_3"]').prop('checked', true)
            }
     }else{
         $('input[id="match"]').prop('checked', true)
         $('input[id="match"]').parent().removeClass('checkbox-success')
         $('input[id="match"]').parent().addClass('checkbox-danger')

         $('input[id="min_8"]').prop('checked', true)
         $('input[id="min_8"]').parent().removeClass('checkbox-success')
         $('input[id="min_8"]').parent().addClass('checkbox-danger')

         $('input[id="lower_case"]').prop('checked', true)
         $('input[id="lower_case"]').parent().removeClass('checkbox-success')
         $('input[id="lower_case"]').parent().addClass('checkbox-danger')

         $('input[id="upper_case"]').prop('checked', true)
         $('input[id="upper_case"]').parent().removeClass('checkbox-success')
         $('input[id="upper_case"]').parent().addClass('checkbox-danger')

         $('input[id="has_num"]').prop('checked', true)
         $('input[id="has_num"]').parent().removeClass('checkbox-success')
         $('input[id="has_num"]').parent().addClass('checkbox-danger')

         $('input[id="has_sp"]').prop('checked', true)
         $('input[id="has_sp"]').parent().removeClass('checkbox-success')
         $('input[id="has_sp"]').parent().addClass('checkbox-danger')

         $('input[id="min_3"]').prop('checked', true)
         $('input[id="min_3"]').parent().removeClass('checkbox-success')
         $('input[id="min_3"]').parent().addClass('checkbox-danger')
        }
     var check = 0
     $('.verification').each(function(){
          if ($(this).hasClass('checkbox-success')){
               check = check + 1
          }
     })

     if (check == 3){
         $('button[type="submit"]').prop('disabled', false)
     }else{
         $('button[type="submit"]').prop('disabled', true)
        }
 })

 $(document).ready(function() {
     $('button[type="submit"]').prop('disabled', true);
 });
