(setq *print-case* :capitalize)

(defparameter *name* 'Lynn)
;; eq is used for symbols
(format t "(eq *name* 'Lynn) = ~d ~%" (eq *name* 'Lynn))
;; equal is used for most stuff
(format t "(equal 'car 'truck) = ~d ~%" (equal 'car 'truck))
(format t "(equal 10 10) = ~d ~%" (equal 10 10))
(format t "(equal string String) = ~d ~%" (equal "string" "String"))

;; equalp is used to compare more loosely like case insensitive 
;;  or floats with integers
(format t "(equalp string String) = ~d ~%" (equalp "string" "StRinG"))
(format t "(equalp 1.0 1) = ~d ~%" (equalp 1.0 1))

;; comparison
(defvar *age* 21)
(if (<= *age* 18)
	(format t "sorry can't vote~%")
	(format t "don't complain go vote ~%"))

(if (or (<= *age* 14) (>= *age* 75)) 
	(format t "Work if you want~%")
	(format t "You should be at work~%")
	)