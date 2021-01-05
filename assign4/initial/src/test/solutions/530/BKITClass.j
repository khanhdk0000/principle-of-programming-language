.source BKITClass.java
.class public BKITClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iload_1
	iconst_1
	if_icmpne Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label6
Label7:
	ldc "1"
	invokestatic io/print(Ljava/lang/String;)V
Label8:
	goto Label2
Label6:
	iload_1
	iconst_2
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label12
Label13:
	ldc "2"
	invokestatic io/print(Ljava/lang/String;)V
Label14:
	goto Label2
Label12:
	iload_1
	iconst_3
	if_icmpne Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label18
Label19:
	ldc "3"
	invokestatic io/print(Ljava/lang/String;)V
Label20:
	goto Label2
Label18:
	iload_1
	iconst_4
	if_icmpne Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	ifle Label24
Label25:
	ldc "4"
	invokestatic io/print(Ljava/lang/String;)V
Label26:
	goto Label2
Label24:
	iload_1
	bipush 7
	if_icmpne Label27
	iconst_1
	goto Label28
Label27:
	iconst_0
Label28:
	ifle Label29
Label31:
	ldc "7"
	invokestatic io/print(Ljava/lang/String;)V
Label32:
	goto Label2
Label30:
	goto Label30
Label29:
	ldc "greater"
	invokestatic io/print(Ljava/lang/String;)V
Label2:
Label30:
Label1:
	return
.limit stack 11
.limit locals 2
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
