function isUrl(s) {
    var regexp = /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/
    return regexp.test(s);
}

(function($){
    $.fn.serializeObject = function(){

        var self = this,
            json = {},
            push_counters = {},
            patterns = {
                "validate": /^[a-zA-Z][a-zA-Z0-9_]*(?:\[(?:\d*|[a-zA-Z0-9_]+)\])*$/,
                "key":      /[a-zA-Z0-9_]+|(?=\[\])/g,
                "push":     /^$/,
                "fixed":    /^\d+$/,
                "named":    /^[a-zA-Z0-9_]+$/
            };


        this.build = function(base, key, value){
            base[key] = value;
            return base;
        };

        this.push_counter = function(key){
            if(push_counters[key] === undefined){
                push_counters[key] = 0;
            }
            return push_counters[key]++;
        };

        $.each($(this).serializeArray(), function(){

            // Skip invalid keys
            if(!patterns.validate.test(this.name)){
                return;
            }

            var k,
                keys = this.name.match(patterns.key),
                merge = this.value,
                reverse_key = this.name;

            while((k = keys.pop()) !== undefined){

                // Adjust reverse_key
                reverse_key = reverse_key.replace(new RegExp("\\[" + k + "\\]$"), '');

                // Push
                if(k.match(patterns.push)){
                    merge = self.build([], self.push_counter(reverse_key), merge);
                }

                // Fixed
                else if(k.match(patterns.fixed)){
                    merge = self.build([], k, merge);
                }

                // Named
                else if(k.match(patterns.named)){
                    merge = self.build({}, k, merge);
                }
            }

            json = $.extend(true, json, merge);
        });

        return json;
    };
})(jQuery);

var success = false;

$(function() {
    $("#basic-example").steps({
        headerTag: "h3",
        bodyTag: "section",
        transitionEffect: "slide"
    }), $("#create-campaign").steps({
        headerTag: "h3",
        bodyTag: "section",
        transitionEffect: "slide",
        stepsOrientation: "vertical",
        onStepChanging: function(event, currentIndex, newIndex) {
            // if (is_async_step) {
            //     is_async_step = false;
            //     //ALLOW NEXT STEP
            //     return true;
            // }
            if(currentIndex == 2 && newIndex == 3){

                var campaign_flights = $("#create-campaign-flights").serialize();
                var campaign_objective = $("#create-campaign-objective").serialize();
                var campaign_pacing_mode = $("#campaign-pacing-mode").serialize();
                var campaign_kpis = $("#campaign-kpi").serialize();
                var campaign_data = campaign_flights+ '&' + campaign_objective +'&' + campaign_pacing_mode + '&' + campaign_kpis;
                $.ajax({
                    type: 'POST',
                    url: "../../campaigns/create-campaign",
                    data: campaign_data,
                    success: function (data) {
                        success = true;
                        return true;
                    },
                    error: function(e, data, settings, exception){
                        console.log(data);
                        console.log(e);
                        alert("Something went wrong while creating Advertiser. Please try again");
                    }
                });
                return true;
            }

            if((currentIndex == 1 && newIndex == 2) || (currentIndex == 3 && newIndex == 2)){
                $("a[href='#next']").text('Create');
            }
            else{
                $("a[href='#next']").text('Next');
            }

            if ($("#create-campaign-objective").valid()){
                return true;
            }
            else{
                return false;
            }
        },
        onFinishing: function(event, currentIndex) {
            return true;
        },
        onFinished: function(event, currentIndex) {
            location.reload();
        }
    })
});
