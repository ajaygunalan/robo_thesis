# the fundamental product of geometric algebra

This chapter's agenda is brutally practical: the "subspace products" you already have (inner/metric information vs outer/spanning information) each throw away something, so neither can be inverted, so you can't *solve* geometry equations with them. The fix is to fuse them into one product that keeps both kinds of information and becomes invertible—then algebra starts behaving like geometry-friendly arithmetic.

The first move is local and geometric: build an invertible product for vectors by packing the symmetric part (metric/inner content) together with the antisymmetric part (spanning/outer content). That construction—and the immediate consequences like noncommutativity except in special alignments—live in [[geometric product for vectors]].

Once you can divide by a vector, ratios stop being vague "proportionality" talk and become computable operators. The chapter's 2D similarity example is really a preview of how "$(b/a)$ acting on $c$" encodes rotation+scaling without ever introducing a matrix; the clean operator viewpoint is unpacked in [[vector ratios as coordinate-free operators]].

Then the chapter resets the foundations: instead of defining the geometric product as "inner + outer", it gives an axiomatic definition tied directly to the metric (scalar squares), and shows you can recover the inner product as the symmetric part via polarization. That "start from the geometric product, derive everything else" story lives in [[clifford axioms and polarization identity]].

With that foundation, you confront the real structural shift: geometric multiplication doesn't preserve grade. Products of k- and l-blades can spill into a whole ladder of grades, with "shared directions" collapsing grade by steps of two. That mental model is the difference between treating GA as a bag of formulas versus seeing why it works; it's captured in [[grade mixing in the geometric product]].

Next, the chapter pays off the promise "you won't need other products": wedge, contractions, and scalar product can all be retrieved from the geometric product—either by symmetry manipulations (with grade involution bookkeeping) or by selecting the right grade parts of a product. That reconstruction—plus the practical reorder identities you use constantly in hand derivations and code—is consolidated in [[recovering subspace products from the geometric product]].

Finally, invertibility stops being abstract and becomes geometry. Once blades have inverses (when non-null), you can express projection and rejection as literal divisions, and you can read "left division vs right division" as producing different geometric effects—most famously reflection as a sandwiching operation. Those operations, and the neat Gram–Schmidt reinterpretation as repeated rejections, are developed in [[geometric division - inverses of vectors and blades]] and then used concretely in [[projection-rejection-reflection-and-ga-gram-schmidt]].

The chapter ends where it should: you now have an associative, invertible product that encodes both measurement and orientation, and a "sandwich" pattern that is obviously begging to be generalized. That generalization—versors/rotors as operators built from products of vectors—is the next chapter's main event.
