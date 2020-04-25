function mediaInformationHTML(userData) {
    if (userData.length == 0) {
        return `<div class="clearfix repo-list">No pictures found!</div>`;
    }

    var listItemsHTML = userData.data.map(function(media) {

        return `<div class="col s3"><img class="materialboxed galery-pic" src="${media.media_url}" alt="Piano Studio Instagram" ></div>`;
    });

    return `${joinObj(listItemsHTML)}`;

}


function fetchInstagramInformation(event) {

    $.when(
        $.getJSON("https://graph.instagram.com/me/media?fields=caption,id,media_type,media_url&access_token=IGQVJWRURFRl9ROUJmNzgyX21yQ3lESnZAQeklILVRFOGpVUXBVY3g0aFFKZAlVFVHZA2WFZARU05uMXgtRFE0dTFCbUhFamdjWWJuZAmNCM1VZAZAmY5VGdIejdDSEVTaVlDTHNYSlY4UGZASLXREQW9SZA0VRYwZDZD")
    ).then(
        function(response) {
            var userData = response;
            $("#sample").html(`<div id="loader2"><p>Loaded</p></div>`);
            $("#sample").html(mediaInformationHTML(userData));
            $('.materialboxed').materialbox();
        }
    );

}

function joinObj(a) {
    var out = [];
    out.push('<h3>Gallery</h3>');
    out.push('<div class="row op s12">');
    for (var i = 0; i < a.length; i++) {
        out.push(a[i]);
        if ((i + 1) % 4 == 0) {
            out.push('</div>');
            out.push('<div class="row op s12">');
        }
    }
    out.push('</div>');
    return out.join("\n");
}
