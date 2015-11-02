var gulp      = require('gulp');
var minifyCss = require('gulp-minify-css');

module.exports = function() {
    return gulp.src('static/**/*.css')
               .pipe(minifyCss())
               // Saves it on dist folder
               .pipe(gulp.dest('dist'));
};
