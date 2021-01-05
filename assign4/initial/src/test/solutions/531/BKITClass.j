.source BKITClass.java
.class public BKITClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is c I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_2
	istore_2
	iconst_3
	istore_3
	iload_1
	iload_2
	iadd
	iload_3
	iadd
	iconst_3
	if_icmple Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label6
Label7:
	iload_1
	iload_2
	iadd
	iconst_2
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label13
Label14:
	iload_1
	iconst_1
	if_icmple Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label20
Label21:
	ldc "a"
	invokestatic io/print(Ljava/lang/String;)V
Label22:
	goto Label16
Label20:
	iload_2
	iconst_1
	if_icmple Label23
	iconst_1
	goto Label24
Label23:
	iconst_0
Label24:
	ifle Label25
Label27:
	ldc "b"
	invokestatic io/print(Ljava/lang/String;)V
Label28:
	goto Label16
Label26:
	goto Label26
Label25:
	ldc "nei"
	invokestatic io/print(Ljava/lang/String;)V
Label16:
Label26:
Label15:
	goto Label9
Label13:
Label9:
Label13:
Label8:
	goto Label2
Label6:
Label2:
Label6:
Label1:
	return
.limit stack 9
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LBKITClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
