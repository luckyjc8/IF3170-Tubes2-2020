;;;;;;;;;;;;;;;;;;;
;;/* DEFTEMPLATE */
;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;
;;/* DEFFACTS    */
;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;
;;/* DEFFUNCTIONS*/
;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;
;;/* DEFRULE 	 */
;;;;;;;;;;;;;;;;;;;

(defrule knRule
	(checkKN ?b ?x ?y ?k ?n)
	(test (> ?n ?k))
	(test (> ?k 0))
=>
	(assert (temptTrue ?b ?x ?y ?k ?n))
	(assert (tempFalse (* ?b -1) ?x ?y ?k ?n))
)

(defrule recursiveCNFtrue
	(temptTrue ?b ?x ?y ?k ?n)
=>
	(assert (checkKN ?b ?x ?y (- ?k 1) (- ?n 1)))
)

(defrule recursiveCNFfalse
	(temptTrue ?b ?x ?y ?k ?n)
=>
	(assert(checkKN ?b ?x ?y ?k (- ?n 1)))
)

(defrule baseKNmine
	(checkKN ?b ?x ?y ?k ?n)
	(test (= ?n ?k))
	(test (= 0 ?k))
=>
	(assert (mine ?b ?x ?y))
)