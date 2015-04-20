#!/usr/local/bin/csi -script

(define (howdy)
  (display "howdy there world!\n"))

(howdy)

(display (string-append "1" "2"))
(newline)

(define my-line
    (lambda (ln)
        (display ln)
        (newline)))

(define inf (open-input-file "example.txt"))
(define lns (read-lines inf))
(for-each my-line lns)
(close-input-port inf)
