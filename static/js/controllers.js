function UserInputCtrl($scope, $location) {
    $scope.username = '';

    $scope.submit = function() {
        $location.path('/' + $scope.username);
    };
}

function LyricsViewCtrl($scope, $http, $routeParams) {
    $scope.username = $routeParams.username;
    $scope.header = 'Loading...';
    $scope.subHeader = 'please wait';

    $http.get('api/lastlyrics/' + $scope.username).
        success(function(data) {
            if (data.data.length > 0) {
                track = data.data[0];
                $scope.header = track.song;
                $scope.subHeader = 'by ' + track.artist;
                $scope.track = track;
            } else {
                $scope.header = 'Not found';
                $scope.subHeader = 'could not find the lyrics or song scrobbed by ' + $scope.username;
            }
        }).
        error(function() {
            $scope.header = 'Error';
            $scope.subHeader = 'sorry, something wrong has happened';
        });
}
