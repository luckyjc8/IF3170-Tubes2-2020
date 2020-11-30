;;;;;;;;;;;;;;;;;;;
;;/* DEFTEMPLATE */
;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;
;;/* DEFFACTS      */
;;;;;;;;;;;;;;;;;;;
(deffacts KN
	()
)
;;****************
;;* DEFFUNCTIONS *
;;****************

;;;;;;;;;;;;;;;;;;;
;;/* DEFRULE */
;;;;;;;;;;;;;;;;;;;


(defrule zeroMine 
	(current 0 ?x ?y)
=>
	(assert (openAdjacent ?x ?y))
)

(defrule matchCurrentClosed
	(current ?n1 ?x1 ?y1)
	(closed ?n2 ?x2 ?y2)
	(test (and (and (eq ?n1 ?n2) (eq ?x1 ?x2)) (eq ?y1 ?y2)))
=>
	(assert (putFlag ?x ?y))
)

(defrule matchCurrentFlagged
	(current ?n1 ?x1 ?y1)
	(flagged ?n2 ?x2 ?y2)
	(test (and (and (eq ?n1 ?n2) (eq ?x1 ?x2)) (eq ?y1 ?y2)))
=>
	(assert (openAdjacent ?x ?y))
)

(defrule knRule
	(KN  ?k ?n)
	(test (> n k))
	(test (> k 0))
=>
	(assert (L ?k ?n))
	(assert (U ?k ?n))
)

(defrule lRule
	(L ?k ?n)
=>
	
)