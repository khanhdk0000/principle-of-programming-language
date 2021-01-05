.source BKITClass.java
.class public BKITClass
.super java.lang.Object
.field static a I
.field static b Ljava/lang/String;
.field static c F

.method public static main([Ljava/lang/String;)V
	iconst_5
	putstatic BKITClass/a I
	ldc "string"
	putstatic BKITClass/b Ljava/lang/String;
	ldc 5.6
	putstatic BKITClass/c F
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic BKITClass/c F
	ldc 5.6
	fcmpl
	ifle Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label6
Label7:
	getstatic BKITClass/c F
	ldc 1.0
	fadd
	putstatic BKITClass/c F
Label8:
	goto Label2
Label6:
Label2:
Label6:
	getstatic BKITClass/c F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic BKITClass/c F
	ldc 6.0
	fcmpl
	ifge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
Label14:
	ldc "yes"
	invokestatic io/print(Ljava/lang/String;)V
Label15:
	goto Label9
Label13:
	goto Label13
Label12:
	ldc "No"
	invokestatic io/print(Ljava/lang/String;)V
Label9:
Label13:
Label1:
	return
.limit stack 5
.limit locals 1
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
