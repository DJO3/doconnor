$(document.links).filter(function() {
    return this.hostname != window.location.hostname && this.protocol != "mailto:";
}).attr('target', '_blank');
