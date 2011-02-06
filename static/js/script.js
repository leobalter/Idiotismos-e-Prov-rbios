jQuery(function($) {
    var $main = $('#main');

    tAPI = {
        key : "AIzaSyBxHfduvWTZZnNaoQgGLOi1K_ox3gTicOc",
        url : "https://www.googleapis.com/language/translate/v2?key=",
        original : {
            txt : escape($main.find('.original').text()),
            src : "pt",
            tgt : "en",
            resp : function(response) {
                tAPI.handleResponse(response, 'original');
            }
        },
        translated : {
            txt : escape($main.find('.translated').text()),
            src : "en",
            tgt : "pt",
            resp : function(response) {
                tAPI.handleResponse(response, 'translated');
            }
        },
        handleResponse : function(response, place) {
            var titulo = '';
            if (place == 'original') {
                titulo = '<h3>A frase original via Google Translate:</h3>';
            } else if (place == 'translated') {
                titulo = '<h3>A frase em inglês de volta ao português via Google Translate:</h3>';
            }
            
            $(titulo+'<p>'+response.data.translations[0].translatedText+'</p>')
                .appendTo('.fromAPI');
        }
    };
    
    var translate1 = '<script src="' + tAPI.url + tAPI.key + '&source='
                   + tAPI.original.src + '&target=' + tAPI.original.tgt
                   + '&callback=tAPI.original.resp&q=' 
                   + tAPI.original.txt + '"></script>';

    var translate2 = '<script src="' + tAPI.url + tAPI.key + '&source='
                   + tAPI.translated.src + '&target=' + tAPI.translated.tgt
                   + '&callback=tAPI.translated.resp&q=' 
                   + tAPI.translated.txt + '"></script>';
    
    $('body').append(translate1);
    $('body').append(translate2);
});



















