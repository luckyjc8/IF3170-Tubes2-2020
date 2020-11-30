;;;;;;;;;;;;;;;;;;;
;;/* DEFTEMPLATE */
;;;;;;;;;;;;;;;;;;;

(deftemplate choosen-cell 
   (slot action 
      ;;/* flag, open, pass */
      (type SYMBOL) 
      (default ?NONE))
   (slot x
      (type INTEGER)
      (default ?NONE))
    (slot y
      (type SYMBOL) 
      (default ?NONE)))

;;/* value = jumlah bom (block yang belum dibuka value = 0, block dengan flag value = -1, border/pojok value = -999) */
(deftemplate right
   (slot value
      (type INTEGER) 
      (default ?NONE))
   (slot x
      (type INTEGER)
      (default ?NONE))
    (slot y
      (type SYMBOL) 
      (default ?NONE)))

(deftemplate left
   (slot value
      (type INTEGER) 
      (default ?NONE))
   (slot x
      (type INTEGER)
      (default ?NONE))
    (slot y
      (type SYMBOL) 
      (default ?NONE)))

(deftemplate up
   (slot value
      (type INTEGER) 
      (default ?NONE))
   (slot x
      (type INTEGER)
      (default ?NONE))
    (slot y
      (type SYMBOL) 
      (default ?NONE)))

(deftemplate down
   (slot value
      (type INTEGER) 
      (default ?NONE))
   (slot x
      (type INTEGER)
      (default ?NONE))
    (slot y
      (type SYMBOL) 
      (default ?NONE)))

(deftemplate up-right
   (slot value
      (type INTEGER) 
      (default ?NONE))
   (slot x
      (type INTEGER)
      (default ?NONE))
    (slot y
      (type SYMBOL) 
      (default ?NONE)))

(deftemplate down-right
   (slot value
      (type INTEGER) 
      (default ?NONE))
   (slot x
      (type INTEGER)
      (default ?NONE))
    (slot y
      (type SYMBOL) 
      (default ?NONE)))

(deftemplate up-left
   (slot value
      (type INTEGER) 
      (default ?NONE))
   (slot x
      (type INTEGER)
      (default ?NONE))
    (slot y
      (type SYMBOL) 
      (default ?NONE)))

(deftemplate down-left
   (slot value
      (type INTEGER) 
      (default ?NONE))
   (slot x
      (type INTEGER)
      (default ?NONE))
    (slot y
      (type SYMBOL) 
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

;;/* ----------- UPDATE NEIGHBOUR -----------*/
(defrule updateNeighbour ""
    (choosen (x ?a))
    (choosen (y ?b))
    =>
    (assert (right(?x + ?a)))
    (assert (left(?x - ?a)))
    (assert (up(?y - ?b)))
    (assert (down(?y + ?b)))
    (assert (down-left(?x - ?a)))
    (assert (down-left(?y + ?b)))
    (assert (up-left(?x - ?a)))
    (assert (up-left(?y - ?b)))
    (assert (up-right(?x + ?a)))
    (assert (up-right(?y - ?b)))
    (assert (down-right(?x + ?a)))
    (assert (down-right(?y + ?b)))
)

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
    (assert (choosen-cell(action flag)))
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
    (assert (choosen-cell(action flag)))
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
    (assert (choosen-cell(action flag)))
)

(defrule threeBomb4 ""
    (up ?value)
    (test (> ?value 0))
    (left ?value)
    (test (> ?value 0))
    (up-left ?value)
    (test (> ?value 0))
    =>
    (assert (choosen-cell(value -1)))
    (assert (choosen-cell(action flag)))
))

;;/* ----------- FLAG BY FLAG -----------*/

(defrule selectByFlag1 ""
    (up ?value)
    (test (> ?value 1))
    (up-left (value -999))
    (up-right ?value)
    (test (> ?value 0))
    (left (value -1))
    =>
    (assert (choosen-cell(value -1)))
    (assert (choosen-cell(action flag)))
)

(defrule selectByFlag2 ""
    (up ?value)
    (test (> ?value 0))
    (up-right (value -999))
    (up-left ?value)
    (test (> ?value 0))
    (right (value -1))
    =>
    (assert (choosen-cell(value -1)))
    (assert (choosen-cell(action flag)))
)

(defrule selectByFlag3 ""
    (down ?value)
    (test (> ?value 0))
    (down-right (value -999))
    (down-left ?value)
    (test (> ?value 0))
    (left (value -1))
    =>
    (assert (choosen-cell(value -1)))
    (assert (choosen-cell(action flag)))
)

;;/* ----------- SELECT BY 1 AND FLAG -----------*/
(defrule selectby1AndFlag ""
    (up (value 1))
    (right (value -1))
)
