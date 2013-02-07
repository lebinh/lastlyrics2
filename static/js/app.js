var app = angular.module('lastlyrics', []);
app.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: 'static/partials/user-input.html',
        controller: UserInputCtrl
    });
    $routeProvider.when('/:username', {
        templateUrl: 'static/partials/lyrics-view.html',
        controller: LyricsViewCtrl
    });
    $routeProvider.otherwise({redirectTo: '/'});
}]);
