/**
 * Books.app
 * A MVC application which displays a list of books and their reviews.
 * Uses nested data which is loaded from a single json file.
 */
Ext.Loader.setConfig({enabled: true});
Ext.application({
    name: 'Books',
    appFolder: 'static/js/app',

    controllers: [
        'Books'
    ],
    
    autoCreateViewport: true
});