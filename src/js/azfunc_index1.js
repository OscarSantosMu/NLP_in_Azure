module.exports = function (context, myQueueItem) {

    context.log('Processing queue message', myQueueItem);
    
    let https = require ('https');
    
    // Reemplaza <YOUR ACCESS KEY HERE> con tu accessKey como string.
    
    let accessKey = '<YOUR ACCESS KEY HERE>';
    
    // Reemplaza [region], incluyendo los corchetes, en el uri de abajo
    
    // Deberás usar la llamada REST API en la misma región en donde creaste el servicio para obtener tu access key
    
    // Por ejemplo, si obtuviste tus claves de la región northeurope, reemplaza
    
    // "westus" en URI de abajo por "northeurope".
    
    let uri = '[region].api.cognitive.microsoft.com';
    
    let path = '/text/analytics/v2.0/sentiment';
    
    let response_handler = function (response) {
    
        let body = '';
        
        response.on ('data', function (chunk) {
        
            body += chunk;
        
        });
        
        response.on ('end', function () {
        
            let body_ = JSON.parse (body);
            
            let body__ = JSON.stringify (body_, null, ' ');
            
            context.log (body__);
            
            context.done();
            
            return;
        
        });
        
        response.on ('error', function (e) {
        
            context.log ('Error: ' + e.message);
            
            context.done();
            
            return;
        
        });
    
    };
    
    let get_sentiments = function (documents) {
    
        let body = JSON.stringify (documents);
        
        let request_params = {
        
            method : 'POST',
            
            hostname : uri,
            
            path : path,
            
            headers : {
            
                'Ocp-Apim-Subscription-Key' : accessKey,
            
            }
        
        };
        
        let req = https.request (request_params, response_handler);
        
        req.write (body);
        
        req.end ();
    
    }
    
    // Crea un arreglo de documentos con una entrada.
    
    let documents = { 'documents': [
    
        {
        
        'id': '1',
        
        'language': 'en',
        
        'text': myQueueItem
        
        },
    
    ]};
    
    get_sentiments (documents);
    
};