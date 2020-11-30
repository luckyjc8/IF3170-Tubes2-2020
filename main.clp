;;;;;;;;;;;;;;;;;;;
;;/* DEFTEMPLATE */
;;;;;;;;;;;;;;;;;;;



(deftemplate chosen-cell 
   (slot action 
      ;;/* flag, open */
      (type SYMBOL) 
      (default ?NONE)))

;;/* value = jumlah bom (block yang belum dibuka value = 0, block dengan flag value = -1, border/pojok value = -999) */
(deftemplate right
   (slot value
      (type INTEGER) 
      (default ?NONE)))

(deftemplate left
   (slot value
      (type INTEGER) 
      (default ?NONE)))

(deftemplate up
   (slot value
      (type INTEGER) 
      (default ?NONE)))

(deftemplate down
   (slot value
      (type INTEGER) 
      (default ?NONE)))

(deftemplate up-right
   (slot value
      (type INTEGER) 
      (default ?NONE)))

(deftemplate down-right
   (slot value
      (type INTEGER) 
      (default ?NONE)))

(deftemplate up-left
   (slot value
      (type INTEGER) 
      (default ?NONE)))

(deftemplate down-left
   (slot value
      (type INTEGER) 
      (default ?NONE)))

;;;;;;;;;;;;;;;;;;;
;;/* DEFFACTS      */
;;;;;;;;;;;;;;;;;;;

;;****************
;;* DEFFUNCTIONS *
;;****************

;;;;;;;;;;;;;;;;;;;
;;/* DEFRULE */
;;;;;;;;;;;;;;;;;;;

;;/* ----------- SORROUNDED BY 1 1 1 -----------*/

(defrule threeBomb1 ""
    (down ?value)
    (test (> ?value 0))
    (left ?value)
    (test (> ?value 0))
    (down-left ?value)
    (test (> ?value 0))
    =>
    (assert (choosen-cell(value -1)))
)

(defrule threeBomb2 ""
    (down ?value)
    (test (> ?value 0))
    (right ?value)
    (test (> ?value 0))
    (down-right ?value)
    (test (> ?value 0))
    =>
    (assert (choosen-cell(value -1)))
)

(defrule threeBomb3 ""
    (up ?value)
    (test (> ?value 0))
    (right ?value)
    (test (> ?value 0))
    (up-right ?value)
    (test (> ?value 0))
    =>
    (assert (choosen-cell(value -1)))
)

(defrule threeBomb3 ""
    (up ?value)
    (test (> ?value 0))
    (left ?value)
    (test (> ?value 0))
    (up-left ?value)
    (test (> ?value 0))
    =>
    (assert (choosen-cell(value -1)))
))

;;/* ----------- SELECT BY FLAG -----------*/

(defrule threeBomb1 ""
    (up ?value)
    (test (> ?value 0))
    (up-left (value -999))
    (up-right ?value)
    (test (> ?value 0))
    (left (value -1))
    =>
    (assert (choosen-cell(value -1)))
)


