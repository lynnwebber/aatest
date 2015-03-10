(defpackage :com.wellkeeper.junk
  (:nicknames :wk-junk)
  (:use :common-lisp)
  (:export :howdy))

(in-package :com.wellkeeper.junk)

(defun howdy ()
	(format t "howdy world from the wk-junk package!!"))

(defun myavg (&rest args)
  (/ (apply #'+ args) (length args)))
