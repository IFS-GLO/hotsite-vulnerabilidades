var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var cssnano = require('gulp-cssnano');

var path = {
  'node': 'node_modules',
  'dist': 'hotsite/hotsite/core/static'
}

// scripts paths
var jsFiles = [
  path.node + '/tether/dist/js/tether.min.js',
  path.node + '/jquery/dist/jquery.min.js',
  path.node + '/popper.js/dist/umd/popper.min.js',
  path.node + '/bootstrap/dist/js/bootstrap.min.js',
  path.node + '/datatables.net-bs4/js/dataTables.bootstrap4.js',
  path.node + '/pace-js/pace.min.js',
  path.node + '/select2/dist/js/select2.min.js',
  path.node + '/toastr/build/toastr.min.js',
]

// styles path
var cssFiles = [
  path.node + '/tether/dist/css/tether.min.css',
  path.node + '/bootstrap/dist/css/bootstrap.min.css',
  path.node + '/font-awesome/css/font-awesome.min.css',
  path.node + '/datatables.net-bs4/css/dataTables.bootstrap4.css',
  path.node + '/select2/dist/css/select2.min.css',
  path.node + '/toastr/build/toastr.min.css',
]

gulp.task('scripts', function () {
  return gulp.src(jsFiles)
    .pipe(concat('all.min.js'))
    .pipe(uglify())
    .pipe(gulp.dest(path.dist + '/js'));
});

gulp.task('styles', function () {
  return gulp.src(cssFiles)
    .pipe(concat('all.min.css'))
    .pipe(cssnano())
    .pipe(gulp.dest(path.dist + '/css'))
});

gulp.task('fonts', function () {
  gulp.src(path.node + '/font-awesome/fonts/**.*')
    .pipe(gulp.dest(path.dist + '/fonts'));
});

gulp.task('default', ['styles', 'scripts', 'fonts']);
