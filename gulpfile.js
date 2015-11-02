var gulp = require('./gulp')([
    'minifyCss'
]);

gulp.task('default', ['minifyCss']);
