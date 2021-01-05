.source BKITClass.java
.class public BKITClass
.super java.lang.Object
.field static a I

.method public static main([Ljava/lang/String;)V
	iconst_1
	putstatic BKITClass/a I
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic BKITClass/a I
Label4:
	getstatic BKITClass/a I
	iconst_5
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
.var 1 is x I from Label7 to Label8
	bipush 100
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label8:
Label2:
	iconst_1
	getstatic BKITClass/a I
	iadd
	putstatic BKITClass/a I
	goto Label4
Label3:
Label1:
	return
.limit stack 4
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
